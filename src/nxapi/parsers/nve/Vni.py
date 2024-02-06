from nxapi.parsers.common import moParser
'''
output:
TABLE_nve_vni
  ROW_nve_vni:list
      if-name: nve1
      vni: 2097152
      mcast: n/a
      vni-state: Up
      mode: 0
      type: L3 [testvrf]
      flags: 0
'''

def createMo(output):
    from nxapi.model.nve.Vni import nveVni
    mos = []
    if 'TABLE_nve_vni' in output:
        if isinstance(output['TABLE_nve_vni']['ROW_nve_vni'], list):
            for vni in output['TABLE_nve_vni']['ROW_nve_vni']:
                vniMo = nveVni()
                moParser(vni,vniMo)
                mos.append(vniMo)
        else:
            vniMo = nveVni()
            moParser(output['TABLE_nve_vni']['ROW_nve_vni'],vniMo)
            mos.append(vniMo)
    return mos