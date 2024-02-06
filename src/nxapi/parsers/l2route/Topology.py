from nxapi.parsers.common import moParser
'''
Output from show l2route topology detail
TABLE_l2route_topology
  ROW_l2route_topology:list
      topo-id: 2000
      topo-name: Vxlan-2097152
      topo-type: VNI
      vni: 2097152
      encap-type: 1
      iod: 0
      if-hdl: 1224736769
      vtep-ip: 10.3.0.4
      emulated-ip: 0.0.0.0
      emulated-ro-ip: 100.10.0.1
      tx-id: 15
      rcvd-flag: 0
      rmac: c47e.e0e3.e7df
      vrf-id: 5
      vmac: c47e.e0e3.e7df
      vmac-ro: 0200.640a.0001
      flags: L3cp
      sub-flags: --
      prev-flags: -
'''

def createMo(output):
    '''
    Create a list of mo objects from the output of show l2route topology detail
    Exclude mos that are of type N/A
    '''
    mos = []
    from nxapi.model.l2route.Topology import l2routeTopology
    if 'TABLE_l2route_topology' not in output:
        return mos
    if isinstance(output['TABLE_l2route_topology']['ROW_l2route_topology'], list):
        for each in output['TABLE_l2route_topology']['ROW_l2route_topology']:
            mo = l2routeTopology()
            moParser(each, mo)
            if mo.topo_type not in ['N/A']:
                mos.append(mo)
    else:
        mo = l2routeTopology()
        moParser(output['TABLE_l2route_topology']['ROW_l2route_topology'], mo)
        if mo.topo_type not in ['N/A']:
            mos.append(mo)
    
    return mos 