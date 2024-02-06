import nxapi.model.baseMo as baseMo


class nveVni(baseMo.baseMo):
    def __init__(self):
        super().__init__(klass='nveVni')
        
    def __repr__(self):
        return f'{self._class}: {self.vni}'
    @classmethod
    def __nxApi__(cls):
        return [f'show nve vni' 
                ]
    @classmethod
    def __parserModule__(cls):
        return 'nxapi.parsers.nve.Vni'
