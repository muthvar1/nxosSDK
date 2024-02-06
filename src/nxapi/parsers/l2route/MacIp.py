from nxapi.parsers.common import moParser
'''
Output from show l2route mac-ip all:
TABLE_l2route_mac_ip
  ROW_l2route_mac_ip:list
      topo-id: 2303
      mac-addr: 0021.010a.0001
      host-ip: 50.30.0.10
      prod-type: BGP
      flags: --
      seq-num: 0
      next-hop1: 10.3.0.2 (Label: 14680067)
      soo: 858665009
      encap-type: 1
'''

def createMo(output):
    mos = []
    from nxapi.model.l2route.MacIp import l2routeMacIp
    if 'TABLE_l2route_mac_ip' not in output:
        return mos
    if isinstance(output['TABLE_l2route_mac_ip']['ROW_l2route_mac_ip'], list):
        for each in output['TABLE_l2route_mac_ip']['ROW_l2route_mac_ip']:
            mo = l2routeMacIp()
            moParser(each, mo)
            mos.append(mo)
    else:
        mo = l2routeMacIp()
        moParser(output['TABLE_l2route_mac_ip']['ROW_l2route_mac_ip'], mo)
        mos.append(mo)
    return mos