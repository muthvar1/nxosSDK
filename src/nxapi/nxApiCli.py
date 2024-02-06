"""
Libary to interact with NX-OS devices using NX-API CLI.
Author: Varghese Muthalaly
Email: vamuthal@cisco.com
"""

import requests
import json
import pprint
import importlib
from nxapi.query.Defines import nxosClassToModelMap

class nxApiCli:
    def __init__(self, host, user, passwd, timeout=120):
        """
        Initialize the nxApiCli object.
        host: Hostname or IP address of the device
        user: Username to login to the device
        passwd: Password to login to the device
        port: Port to connect to. Default is 80
        proto: Protocol to use. Default is http
        timeout: Timeout value in seconds. Default is 30
        """
        self.host = host
        self.user = user
        self.passwd = passwd
        #self.port = port
        #self.proto = proto
        self.timeout = timeout
        self.url = f'https://{host}/ins'
        #self.url = proto + '://' + host + '/ins'
        self.headers = {'content-type': 'application/json-rpc'}

    def sendCmd(self, cmd):
        """
        Send a command or list of commands to the device.
        cmd: Command or list of commands to send to the device
        """
        if isinstance(cmd, str):
            cmds = [cmd]
        elif isinstance(cmd, list):
            cmds = cmd
        else:
            raise ValueError("Invalid command type. Expected string or list.")
        

        
        payload = []
        for i in range(1,len(cmds)+1):
            cmd = cmds[i-1]
            data = {
                'jsonrpc': '2.0',
                'method': 'cli',
                'params': {
                    'cmd': cmd,
                    'version': 1
                },
                'id': i
            }
            payload.append(data)
        try:
            print('Sending command: ' + str(cmds))
            response = requests.post(
                self.url,
                data=json.dumps(payload),
                headers=self.headers,
                auth=(self.user, self.passwd),
                timeout=self.timeout,
                verify=False
            )
        except requests.exceptions.RequestException as e:
            print(e)
            raise(e)
        except Exception as e:
            print(e)
            raise(e)
        
        if response.status_code == 200:
            if response.json()['result'] in [None, '', 'null']:
                return None
            return response.json()['result']['body']
        else:
            print('Error sending command: ' + str(cmds))
            print('Status Code: ' + str(response.status_code))
            print('Response: ' + response.text)
            raise Exception('Error sending command: ' + str(cmds))
    
    def sendCmds(self, cmds):
        """
        Send a list of commands to the device.
        cmds: List of commands to send to the device
        """
        return self.sendCmd(cmds)
        
    

    def lookupByClass(self, class_name,pfilter=None):
        """
        This API is used to lookup and return object of the specific class in the NXOS switch. The class name is case sensitive.
        The class name to model translation will be defined in the Defines.py file. The class name should be the same as the
        class name defined in the model file.
        The Defines file will have each class name mapped to its corresponding model file and the class name in the model file.
        e.g: evpnRoute = ('NXOS.model.evpn.Routes','evpnRoute')
        Parameters
            nx_handle: nxapi handle object
                The handle of the connected Nexus device.
            class_name: str
                The name of the class object to be looked up. e.g: evpnRoute
            pfilter: str
                The filter to be applied to the class object. e.g: 'vni==1000'
                The format only supports the syntax of 'property==value' or 'property!=value'

        Returns
            On success, returns the list of objects of the specified class.
        """
        modelModule, className = getattr(nxosClassToModelMap, class_name)
        model = importlib.import_module(modelModule)
        klass = getattr(model, className)
        if pfilter:
            if '==' in pfilter:
                mos = klass.__createMo__(nxHandle=self)
                property = pfilter.split('==')[0]
                value = pfilter.split('==')[1]
                return [mo for mo in mos if getattr(mo, property) == value]
                
            elif '!=' in pfilter:
                mos = klass.__createMo__(nxHandle=self)
                property = pfilter.split('!=')[0]
                value = pfilter.split('!=')[1]
                return [mo for mo in mos if getattr(mo, property) != value]
                
            else:
                raise Exception(f'Invalid filter {pfilter}')
        return klass.__createMo__(nxHandle=self)

def print_nested_keys(data, indent=''):
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, (dict, list)):
                if isinstance(value, dict):print(f"{indent}{key}")
                if isinstance(value, list):print(f"{indent}{key}:list")
                print_nested_keys(value, indent + '  ')
            else:
                print(f"{indent}{key}: {value}")
    elif isinstance(data, list):
        for item in data:
            print_nested_keys(item, indent + '  ')
            break



