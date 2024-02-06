import nxapi.model.baseMo as baseMo






class evpnRoute(baseMo.baseMo):
    #_instances = []
    def __init__(self):
        super().__init__(klass='evpnRoute')
        
    def __repr__(self):
        return f'{self._class}: {self.nonipprefix}'
    @classmethod
    def __nxApi__(cls, vrf_name=None):
        if vrf_name in [None, 'all']:
            return [f'show bgp l2vpn evpn route-type 2',
                    f'show bgp l2vpn evpn route-type 3',
                    f'show bgp l2vpn evpn route-type 4',
                    f'show bgp l2vpn evpn route-type 5'
                    ]
        return [f'show bgp l2vpn evpn route-type 2 vrf {vrf_name}',
                f'show bgp l2vpn evpn route-type 3 vrf {vrf_name}',
                f'show bgp l2vpn evpn route-type 4 vrf {vrf_name}',
                f'show bgp l2vpn evpn route-type 5 vrf {vrf_name}'
                ]
    @classmethod
    def __parserModule__(cls):
        return 'nxapi.parsers.evpn.Routes'