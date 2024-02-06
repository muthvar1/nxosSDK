
'''
output:
{'TABLE_vrf': {'ROW_vrf': [{'TABLE_tib': {'ROW_tib': [{'tib_af': 'IPv6',
                                                       'tib_id': 0,
                                                       'tib_nonce': '0x80000001',
                                                       'tib_state': 'Up'},
                                                      {'tib_af': 'IPv4',
                                                       'tib_id': 0,
                                                       'tib_nonce': '0x00000001',
                                                       'tib_state': 'Up'}]},
                            'max_routes': 0,
                            'mid_threshold': 0,
                            'rd': '0:0',
                            'vni': 0,
                            'vpnid': 'unknown',
                            'vrf_id': 1,
                            'vrf_name': 'default',
                            'vrf_state': 'Up'},
                           {'TABLE_tib': {'ROW_tib': [{'tib_af': 'IPv6',
                                                       'tib_id': 0,
                                                       'tib_nonce': '0x80000002',
                                                       'tib_state': 'Up'},
                                                      {'tib_af': 'IPv4',
                                                       'tib_id': 0,
                                                       'tib_nonce': '0x00000002',
                                                       'tib_state': 'Up'}]},
                            'max_routes': 0,
                            'mid_threshold': 0,
                            'rd': '0:0',
                            'vni': 0,
                            'vpnid': 'unknown',
                            'vrf_id': 2,
                            'vrf_name': 'management',
                            'vrf_state': 'Up'},
                           {'TABLE_tib': {'ROW_tib': [{'tib_af': 'IPv6',
                                                       'tib_id': 0,
                                                       'tib_nonce': '0x80000003',
                                                       'tib_state': 'Up'},
                                                      {'tib_af': 'IPv4',
                                                       'tib_id': 0,
                                                       'tib_nonce': '0x00000003',
                                                       'tib_state': 'Up'}]},
                            'max_routes': 0,
                            'mid_threshold': 0,
                            'rd': '10.2.0.3:4',
                            'vni': 2097152,
                            'vpnid': 'unknown',
                            'vrf_id': 4,
                            'vrf_name': 'testvrf',
                            'vrf_state': 'Up'}]}}


'''
def createMo(output):
    from nxapi.model.l3.Vrf import l3Vrf
    mos = []
    def parseVrf(vrf):
        vrfMo = l3Vrf()
        vrfMo.vrf_name = vrf['vrf_name']
        vrfMo.vrf_id = vrf['vrf_id']
        vrfMo.vrf_state = vrf['vrf_state']
        vrfMo.rd = vrf['rd']
        vrfMo.vni = vrf['vni']
        vrfMo.vpnid = vrf['vpnid']
        vrfMo.max_routes = vrf['max_routes']
        vrfMo.mid_threshold = vrf['mid_threshold']
        vrfMo.tib = []
        for tib in vrf['TABLE_tib']['ROW_tib']:
            tibData = {}
            tibData['tib_af'] = tib['tib_af']
            tibData['tib_id'] = tib['tib_id']
            tibData['tib_state'] = tib['tib_state']
            tibData['tib_nonce'] = tib['tib_nonce']
            vrfMo.tib.append(tibData)
        return vrfMo
    
    if 'TABLE_vrf' in output:
        if isinstance(output['TABLE_vrf']['ROW_vrf'], list):
            for vrf in output['TABLE_vrf']['ROW_vrf']:
                mos.append(parseVrf(vrf))
        else:
            mos.append(parseVrf(output['TABLE_vrf']['ROW_vrf']))
    
    return mos
            
        