import nxapi.model.baseMo as baseMo

class l2routeMac(baseMo.baseMo):
    #_instances = []
    def __init__(self):
        super().__init__(klass='l2routeMac')
        
    def __repr__(self):
        return f'{self._class}: {self.mac_addr}'
    @classmethod
    def __nxApi__(cls,topo_id=None):
        if topo_id in [None, 'all']:
            return [f'show l2route mac all detail',
                    ]
        return [f'show l2route mac topology {topo_id} detail',
                ]
    @classmethod
    def __parserModule__(cls):
        return 'nxapi.parsers.l2route.Mac'