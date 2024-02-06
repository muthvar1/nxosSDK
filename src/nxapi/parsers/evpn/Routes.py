import re
'''
TABLE_vrf
  ROW_vrf
    vrf-name-out: default
    TABLE_afi
      ROW_afi
        afi: 25
        TABLE_safi
          ROW_safi
            safi: 70
            af-name: L2VPN EVPN
            TABLE_rd
              ROW_rd:list
                  rd_val: 101:2097152
                  TABLE_prefix
                    ROW_prefix:list
                        nonipprefix: [5]:[0]:[0]:[16]:[50.20.0.0]/224
                        prefixversion: 129
                        totalpaths: 2
                        bestpathnr: 2
                        on-newlist: false
                        on-xmitlist: true
                        suppressed: false
                        needsresync: false
                        locked: false
                        table-map-filtered: false
                        TABLE_path
                          ROW_path:list
                              pathnr: 0
                              policyincomplete: false
                              pathvalid: true
                              pathbest: false
                              pathreoriginated: false
                              pathdeleted: false
                              pathstaled: false
                              pathhistory: false
                              pathovermaxaslimit: false
                              pathmultipath: false
                              pathnolabeledrnh: true
                              pathlocator: false
                              gwip: 0.0.0.0
                              aspath: 101
                              source: external
                              ipnexthop: 100.10.0.2
                              nexthopmetric: 0
                              neighbor: 10.12.0.5
                              neighborid: 10.12.0.5
                              origin: incomplete
                              metric: 1
                              localpref: 100
                              weight: 0
                              inlabel: 2097152
                              TABLE_extcommunity
                                ROW_extcommunity
                                  extcommunity: Extcommunity: RT:100:2097152 ENCAP:8 Router MAC:0200.640a.0002

'''

def createMo(output):
    from nxapi.model.evpn.Routes import evpnRoute
    from nxapi.model.evpn.Path import evpnPath
    mos = []
    def addPath(path):
        pathMo = evpnPath()
        if 'TABLE_importdests' in path:
            if isinstance(path['TABLE_importdests']['ROW_importdests'], list):
                for importdest in path['TABLE_importdests']['ROW_importdests']:
                    try:
                        pathMo.__getattr__('importdest')
                        pathMo.importdest.append(importdest['importdest'])
                    except AttributeError:
                        pathMo._baseMo__addAttr('importdest', [])
                        pathMo.importdest.append(importdest['importdest'])
                    
            else:
                pathMo._baseMo__addAttr('importdest', [path['TABLE_importdests']['ROW_importdests']['importdest']])
            
            pathMo._baseMo__addAttr('importdestscount', path.get('importdestscount', None))

        if 'TABLE_clusterlist' in path:
            if isinstance(path['TABLE_clusterlist']['ROW_clusterlist'], list):
                for clusterlist in path['TABLE_clusterlist']['ROW_clusterlist']:
                    try:
                        pathMo.__getattr__('clusterlist')
                        pathMo.clusterlist.append(clusterlist['clusterlist'])
                    except AttributeError:
                        pathMo._baseMo__addAttr('clusterlist', [])
                        pathMo.clusterlist.append(clusterlist['clusterlist'])
                    
            else:
                pathMo._baseMo__addAttr('clusterlist', [path['TABLE_clusterlist']['ROW_clusterlist']['clusterlist']])
        pathMo._baseMo__addAttr('pathnr', path['pathnr'])
        pathMo._baseMo__addAttr('policyincomplete', path['policyincomplete'])
        pathMo._baseMo__addAttr('pathvalid', path['pathvalid'])
        pathMo._baseMo__addAttr('pathbest', path['pathbest'])
        pathMo._baseMo__addAttr('pathreoriginated', path['pathreoriginated'])
        pathMo._baseMo__addAttr('pathdeleted', path['pathdeleted'])
        pathMo._baseMo__addAttr('pathstaled', path['pathstaled'])
        pathMo._baseMo__addAttr('pathhistory', path['pathhistory'])
        pathMo._baseMo__addAttr('pathovermaxaslimit', path['pathovermaxaslimit'])
        pathMo._baseMo__addAttr('pathmultipath', path['pathmultipath'])
        pathMo._baseMo__addAttr('pathnolabeledrnh', path['pathnolabeledrnh'])
        pathMo._baseMo__addAttr('pathlocator', path['pathlocator'])
        pathMo._baseMo__addAttr('gwip', path.get('gwip', None))
        pathMo._baseMo__addAttr('aspath', path.get('aspath', None))
        pathMo._baseMo__addAttr('originatorid', path.get('originatorid', None))
        pathMo._baseMo__addAttr('source', path.get('source', None))
        pathMo._baseMo__addAttr('ipnexthop', path['ipnexthop'])
        pathMo._baseMo__addAttr('nexthopmetric', path['nexthopmetric'])
        pathMo._baseMo__addAttr('neighbor', path['neighbor'])
        pathMo._baseMo__addAttr('neighborid', path['neighborid'])
        pathMo._baseMo__addAttr('origin', path['origin'])
        pathMo._baseMo__addAttr('metric', path.get('metric', None))
        pathMo._baseMo__addAttr('localpref', path['localpref'])
        pathMo._baseMo__addAttr('weight', path['weight'])
        pathMo._baseMo__addAttr('inlabel', path.get('inlabel', None))
        if 'TABLE_extcommunity' in path:
            if isinstance(path['TABLE_extcommunity']['ROW_extcommunity'], list):
                for extcommunity in path['TABLE_extcommunity']['ROW_extcommunity']:
                    try:
                        pathMo.__getattr__('extcommunity')
                        pathMo.extcommunity.append(extcommunity['extcommunity'])
                    except AttributeError:
                        pathMo._baseMo__addAttr('extcommunity', [])
                        pathMo.extcommunity.append(extcommunity['extcommunity'])
                    
            else:
                pathMo._baseMo__addAttr('extcommunity',[path['TABLE_extcommunity']['ROW_extcommunity']['extcommunity']])
        
        return pathMo
    

    def addPrefix(prefix,kwargs):
        mo = evpnRoute()
        for key, value in kwargs.items():
            mo._baseMo__addAttr(key, value)
        mo._baseMo__addAttr('nonipprefix', prefix['nonipprefix'])
        nonipprefix = extract_evpn_route_info(prefix['nonipprefix'])
        if isinstance(nonipprefix, dict):
            for key, value in nonipprefix.items():
                mo._baseMo__addAttr(key, value)
        mo._baseMo__addAttr('prefixversion', prefix['prefixversion'])
        mo._baseMo__addAttr('totalpaths', prefix['totalpaths'])
        mo._baseMo__addAttr('bestpathnr', prefix['bestpathnr'])
        mo._baseMo__addAttr('on_newlist', prefix['on-newlist'])
        mo._baseMo__addAttr('on_xmitlist', prefix['on-xmitlist'])
        mo._baseMo__addAttr('suppressed', prefix['suppressed'])
        mo._baseMo__addAttr('needsresync', prefix['needsresync'])
        mo._baseMo__addAttr('locked', prefix['locked'])
        mo._baseMo__addAttr('table_map_filtered', prefix['table-map-filtered'])
        if isinstance(prefix['TABLE_path']['ROW_path'], list):
            for path in prefix['TABLE_path']['ROW_path']:
                pathMo = addPath(path)
                mo._baseMo__addChild(pathMo)
        else:
            pathMo = addPath(prefix['TABLE_path']['ROW_path'])
            mo._baseMo__addChild(pathMo)
        return mo
        
    
    def addRd(rd):
        moList = []
        kwargs = {}
        kwargs['vrf_name'] = vrf_name
        kwargs['afi'] = afi
        kwargs['safi'] = safi
        kwargs['router_id'] = router_id
        kwargs['table_version'] = table_version
        
        kwargs['rd_val'] = rd['rd_val']
        kwargs['rd_vrf'] = rd.get('vrf', None)
        kwargs['rd_vniid'] = rd.get('vniid', None)
        if 'TABLE_advertisedto' in rd:
            if isinstance(rd['TABLE_advertisedto']['ROW_advertisedto'], list):
                for advertisedto in rd['TABLE_advertisedto']['ROW_advertisedto']:
                    if not kwargs.get('advertisedto', None):
                        kwargs['advertisedto'] = []
                        kwargs.advertisedto.append(advertisedto['advertisedto'])
                    else:
                        kwargs['advertisedto'] = []
                        kwargs.advertisedto.append(advertisedto['advertisedto'])
            else:
                kwargs['advertisedto'] = [rd['TABLE_advertisedto']['ROW_advertisedto']['advertisedto']]
        try:
            if isinstance(rd['TABLE_prefix']['ROW_prefix'], list):
                for prefix in rd['TABLE_prefix']['ROW_prefix']:
                    moList.append(addPrefix(prefix,kwargs))
            else:
                moList.append(addPrefix(rd['TABLE_prefix']['ROW_prefix'],kwargs))
                
            
            # print (f'Added {len(mo._children)} paths to {mo.nonipprefix}')
        except Exception as e:
            print(f'Error creating evpnRoute object: {e}')
            import pprint
            pprint.pprint(rd)
            import sys
            import pdb; pdb.set_trace()
        return moList
    
    vrf_name = output['TABLE_vrf']['ROW_vrf']['vrf-name-out']
    afi = output['TABLE_vrf']['ROW_vrf']['TABLE_afi']['ROW_afi']['afi']
    safi = output['TABLE_vrf']['ROW_vrf']['TABLE_afi']['ROW_afi']['TABLE_safi']['ROW_safi']['safi']
    router_id = output['TABLE_vrf']['ROW_vrf']['TABLE_afi']['ROW_afi']['TABLE_safi']['ROW_safi'].get('router-id', None)
    table_version = output['TABLE_vrf']['ROW_vrf']['TABLE_afi']['ROW_afi']['TABLE_safi']['ROW_safi'].get('table-version', None)
    if 'TABLE_rd' not in output['TABLE_vrf']['ROW_vrf']['TABLE_afi']['ROW_afi']['TABLE_safi']['ROW_safi']:
        #print (f'No routes found for {vrf_name} {afi} {safi}')
        return mos
    if isinstance(output['TABLE_vrf']['ROW_vrf']['TABLE_afi']['ROW_afi']['TABLE_safi']['ROW_safi']['TABLE_rd']['ROW_rd'], list):
        for rd in output['TABLE_vrf']['ROW_vrf']['TABLE_afi']['ROW_afi']['TABLE_safi']['ROW_safi']['TABLE_rd']['ROW_rd']:
            mos.extend(addRd(rd))
    else:
        mos.extend(addRd(output['TABLE_vrf']['ROW_vrf']['TABLE_afi']['ROW_afi']['TABLE_safi']['ROW_safi']['TABLE_rd']['ROW_rd']))
    
    return mos



            




def extract_evpn_route_info(route_string):
    route_type = re.search(r'\[([\d]+)\]', route_string).group(1)

    if route_type == '5':
        match = re.match(r'\[([\d]+)\]:\[([\d]+)\]:\[([\d]+)\]:\[([\d]+)\]:\[([\w.]+)\]/(\d+)', route_string)
        if match:
            groups = match.groups()
            return {
                'Route_Type': route_type,
                'RD_Length': groups[1],
                'ETag_Length': groups[2],
                'ETag_Value': groups[3],
                'IP_Address': groups[4],
                'Prefix_Length': groups[5]
            }

    elif route_type == '2':
        match = re.match(r'\[([\d]+)\]:\[([\d]+)\]:\[([\d]+)\]:\[([\w.]+)\]:\[(.*?)\]:\[(\d+)?\]:\[(.*?)\]/(\d+)', route_string)
        if match:
            groups = match.groups()
            return {
                'Route_Type': route_type,
                'RD_Length': groups[1],
                'ETag_Length': groups[2],
                'ETag_Value': groups[3],
                'MAC_Address': groups[4],
                'IP_Length': groups[5] if groups[5] else '0',
                'IP_Address': groups[6] if groups[6] else '0.0.0.0',
                'Prefix_Length': groups[7]
            }

    elif route_type == '3':
        match = re.match(r'\[([\d]+)\]:\[([\d]+)\]:\[([\d]+)\]:\[(.*?)\]/(\d+)', route_string)
        if match:
            groups = match.groups()
            return {
                'Route_Type': route_type,
                'RD_Length': groups[1],
                'ETag_Length': groups[2],
                'IP_Address': groups[3],
                'Prefix_Length': groups[4]
            }

    elif route_type == '4':
        match = re.match(r'\[([\d]+)\]:\[([\w.]+)\]:\[(\d+)?\]:\[(.*?)\]/(\d+)', route_string)
        if match:
            groups = match.groups()
            return {
                'Route_Type': route_type,
                'ETag_Value': groups[1],
                'IP_Length': groups[2] if groups[2] else '0',
                'IP_Address': groups[3] if groups[3] else '0.0.0.0',
                'Prefix_Length': groups[4]
            }

    return None