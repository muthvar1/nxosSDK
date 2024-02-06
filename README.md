# NXAPI

An SDK for Cisco NXOS that brings ACI cobra sdk like constructs to the nxos world


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install nxapi.

```bash
python3 -m pip install --upgrade 

```

## Usage

```bash

from nxapi.model.evpn.Routes import evpnRoute
from nxapi.model.evpn.Session import evpnSession
from nxapi.model.nve.Peer import nvePeer
from nxapi.model.nve.Vni import nveVni
from nxapi.model.l3.Vrf import l3Vrf
from nxapi.model.bgp.Session import bgpSession
from nxapi.nxApiCli import nxApiCli
import pprint
from rich.console import Console
_console=Console(highlight=False)
highlight_style = "bold white on #049fd9"
pageSeparator = "bold yellow on #049fd9"
def richPrint(msg):
    text = f'[{highlight_style}]{msg}[/{highlight_style}]'
    _console.print('\n')
    _console.print(text)
    _console.print('\n')

def linePrint(msg):
    _console.print(f'[{pageSeparator}]{msg}[/{pageSeparator}]')


richPrint('We use the nxApiCli class to connect to the switch')
nx = nxApiCli(host = 'ifav11-leaf27.cisco.com', user='admin', passwd='ins3965!',timeout=60)



richPrint('We use the sendCmd method to send a command to the switch')
output = nx.sendCmd('show nve vni')
pprint.pprint(output)



richPrint('We use the __createMo__ method to create a list of objects from the output')
mos = l3Vrf.__createMo__(nxHandle=nx)

richPrint('The mos are reprsented by className: Significant_attribute. e.g: l3Vrf: vrf_name')
print (mos)



richPrint('If we richPrint the individual mos, we get the attributes and their values')
print (mos[0])



richPrint('We can also filter a specific mo from a class with some optional parameters')
mos = l3Vrf.__createMo__(nxHandle=nx, vrf_name='default')

richPrint('We can also fetch the children of the mo. In this case, the children of l3Vrf are bgpSession, evpnSession, evpnRoute')
richPrint('The children are also represented by className: Significant_attribute. e.g: bgpSession: peer_ip')
mos[0].__fetchChildren__(nxHandle=nx)
print (mos[0]._children)



richPrint('Once the children are fetched, you can also access the children directly from the parent mo by referencing the child class name as mo._childClassName')
print (mos[0]._bgpSession)



richPrint('We can also fetch mos by the aci familiar method of lookupByClass')
mos = nx.lookupByClass('l3Vrf')
print (mos)



richPrint("We can also filter the mos by using the pfilter parameter. Note: Currently, the pfilter only supports the syntax of 'property==value' or 'property!=value'")
mos = nx.lookupByClass('l3Vrf', pfilter='vrf_name==default')
print (mos)

richPrint("We can use the mos to fetch the children of the mos as before")
for mo in mos:
    mo.__fetchChildren__(nxHandle=nx)

print (mo._children[0])


```

## Contributing

Pull requests are welcome. For changes, please open a CDETS defect first
to discuss what you would like to change. All commits have to be code-reviewed and unit-tested.

Please make sure to update tests as appropriate.


## License


