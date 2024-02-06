import nxapi.model.baseMo as baseMo

class l2routeMacIp(baseMo.baseMo):
    #_instances = []
    def __init__(self):
        super().__init__(klass='l2routeMacIp')
        
    def __repr__(self):
        return f'{self._class}: {self.mac_addr},{self.host_ip}'
    @classmethod
    def __nxApi__(cls,topo_id=None):
        if topo_id in [None, 'all']:
            return [f'show l2route mac-ip all detail',
                    ]
        return [f'show l2route mac-ip topology {topo_id} detail',
                ]
    @classmethod
    def __parserModule__(cls):
        return 'nxapi.parsers.l2route.MacIp'