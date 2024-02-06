import nxapi.model.baseMo as baseMo


class bgpSession(baseMo.baseMo):
    def __init__(self):
        super().__init__(klass='bgpSession')
        
    def __repr__(self):
        return f'{self._class}: {self.neighbor_id}'
    @classmethod
    def __nxApi__(cls,vrf_name = None):
        if vrf_name in [None, 'all']:
            return ['show bgp sessions'
                ]
        return [f'show bgp sessions vrf {vrf_name}'
                ]
    @classmethod
    def __parserModule__(cls):
        return 'nxapi.parsers.bgp.Session'
