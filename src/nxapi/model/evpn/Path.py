import nxapi.model.baseMo as baseMo






class evpnPath(baseMo.baseMo):
    #_instances = []
    def __init__(self):
        super().__init__(klass='evpnPath')
        #evpnPath._instances.append(self)

    def __str__(self):
        return f'{self._class}: {self.ipnexthop}'
    def __repr__(self):
        return f'{self._class}: {self.ipnexthop}'