import nxapi.model.baseMo as baseMo


class nvePeer(baseMo.baseMo):
    def __init__(self):
        super().__init__(klass='nvePeer')
        
    def __repr__(self):
        return f'{self._class}: {self.peer_ip}'
    @classmethod
    def __nxApi__(cls):
        return [f'show nve peers detail' 
                ]
    @classmethod
    def __parserModule__(cls):
        return 'nxapi.parsers.nve.Peer'
