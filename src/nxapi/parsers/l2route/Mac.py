from nxapi.parsers.common import moParser
'''
Output from show l2route mac all:
TABLE_l2route_mac
  ROW_l2route_mac:list
      topo-id: 2000
      mac-addr: 0200.0a03.0002
      prod-type: VXLAN
      flags: Rmac
      seq-num: 0
      next-hop1: 10.3.0.2
'''

def createMo(output):
    mos = []
    from nxapi.model.l2route.Mac import l2routeMac
    if 'TABLE_l2route_mac' not in output:
        return mos
    if isinstance(output['TABLE_l2route_mac']['ROW_l2route_mac'], list):
        for each in output['TABLE_l2route_mac']['ROW_l2route_mac']:
            mo = l2routeMac()
            moParser(each, mo)
            mos.append(mo)
    else:
        mo = l2routeMac()
        moParser(output['TABLE_l2route_mac']['ROW_l2route_mac'], mo)
        mos.append(mo)
    return mos
