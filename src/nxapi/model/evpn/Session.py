import nxapi.model.baseMo as baseMo






class evpnSession(baseMo.baseMo):
    def __init__(self):
        super().__init__(klass='evpnSession')
        
    def __repr__(self):
        return f'{self._class}: {self.neighbor}'
    @classmethod
    def __nxApi__(cls, vrf_name=None):
        if vrf_name in [None, 'all']:
            return [f'show bgp l2vpn evpn neighbors ',
                    ]
        return [f'show bgp l2vpn evpn neighbors vrf {vrf_name}',
                ]
    @classmethod
    def __parserModule__(cls):
        return 'nxapi.parsers.evpn.Session'