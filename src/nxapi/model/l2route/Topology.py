import nxapi.model.baseMo as baseMo






class l2routeTopology(baseMo.baseMo):
    #_instances = []
    def __init__(self):
        super().__init__(klass='l2routeTopology')
        
    def __repr__(self):
        return f'{self._class}: {self.topo_id}'
    @classmethod
    def __nxApi__(cls):
        return [f'show l2route topology detail',
                ]
    def __childModules__(self):
        '''
        send a list of tuples with the following format:
        (module, className, parentKeyforCli)
        '''
        return [('nxapi.model.l2route.Mac', 'l2routeMac', 'topo_id'),
                ('nxapi.model.l2route.MacIp', 'l2routeMacIp', 'topo_id')
                ]
                
    @classmethod
    def __parserModule__(cls):
        return 'nxapi.parsers.l2route.Topology'