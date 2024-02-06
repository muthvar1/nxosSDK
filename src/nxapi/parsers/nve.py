'''
Parser for nxOs api cli command outputs
Following commands are supported:
show nve peers

show nve interface nve<id> detail

show nve vni

show nve vni summary

show nve vni ingress-replication

show nve multisite dci-links

show nve multisite fabric-links
'''

from . import common


def show_nve_peers(output):
    '''
    Parser for show nve peers
    '''
    # Example output in dictionary format:
    # 
    # {'TABLE_nve_peers': {'ROW_nve_peers': [{'if-name': 'nve1',
    #                                     'learn-type': 'CP',
    #                                     'peer-ip': '10.3.0.1',
    #                                     'peer-state': 'Up',
    #                                     'router-mac': '3c13.cc2e.e087',
    #                                     'uptime': '11:17:29'},
    #                                    {'if-name': 'nve1',
    #                                     'learn-type': 'CP',
    #                                     'peer-ip': '100.10.0.3',
    #                                     'peer-state': 'Up',
    #                                     'router-mac': '0200.640a.0003',
    #                                     'uptime': '03:41:44'}]}}

    # Return list of all nve peers
    return common.common_parser(output,'nve_peers')

def show_nve_interface_detail(output):
    '''
    Parser for show nve interface nve<id> detail
    '''
    # Example output in dictionary format:
    # 
    # {'TABLE_nve_if': {'ROW_nve_if': {'encap-type': 'VXLAN',
    #                              'host-reach-mode': 'Control-Plane',
    #                              'if-name': 'nve1',
    #                              'if-state': 'Up',
    #                              'local-rmac': 'c47e.e0e3.e7df',
    #                              'primary-ip': '10.3.0.4',
    #                              'secondary-ip': '0.0.0.0',
    #                              'source-if': 'loopback1',
    #                              'vpc-capability': 'VPC-VIP-Only '
    #                                                '[not-notified]'}}}
    return common.common_parser(output,'nve_if')