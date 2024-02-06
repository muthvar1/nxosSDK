import nxapi.model.baseMo as baseMo


class l3Vrf(baseMo.baseMo):
    def __init__(self):
        super().__init__(klass='l3Vrf')

    def __repr__(self):
        return f'{self._class}: {self.vrf_name}'
    def __childModules__(self):
        '''
        send a list of tuples with the following format:
        (module, className, parentKeyforCli)
        '''
        return [('nxapi.model.evpn.Routes', 'evpnRoute', 'vrf_name'),
                ('nxapi.model.bgp.Session', 'bgpSession', 'vrf_name'),
                ('nxapi.model.evpn.Session', 'evpnSession', 'vrf_name')
                ]
    
    @classmethod
    def __nxApi__(cls,vrf_name=None):
        if vrf_name in [None, 'all']:
            return ['show vrf detail'
                ]
        return [f'show vrf {vrf_name} detail'
                ]
    @classmethod
    def __parserModule__(cls):
        return 'nxapi.parsers.l3.Vrf'

    