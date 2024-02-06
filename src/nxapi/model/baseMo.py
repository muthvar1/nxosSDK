import importlib
class baseMo(object):
    def __init__(self,klass):
        self._class = klass
        self._children = []
    def __addChild(self, child):
        if not hasattr(self, f'_{child._class}'):
            setattr(self, f'_{child._class}', [])
        getattr(self, f'_{child._class}').append(child)    
        self._children.append(child)
    def __addAttr(self, attr, value):
        setattr(self, attr, value)
    def __addProp(self, prop, value):
        setattr(self, prop, value)
    def __str__(self):
        msg = f'class: {self._class}\n'
        for attr in self.__dict__:
            if not attr.startswith('_'):
                msg += f'{attr} : {self.__dict__[attr]}\n'
        return msg
        #return self._class
    def __repr__(self):
        return self._class
    def __getattr__(self, attr):
        if attr in self.__dict__:
            return self.__dict__[attr]
        else:
            raise AttributeError(f'{self._class} object has no attribute {attr}')
    # def __iter__(cls):
    #     return iter(cls._instances)
    
    def __printMo__(self):
        '''
        print all the attributes and their values for this object
        '''
        for attr in self.__dict__:
            print(f'{attr} = {self.__dict__[attr]}')
    def __printChildren__(self):
        '''
        print all the children of this object
        '''
        for child in self._children:
            print(child)
    def __printProps__(self):
        '''
        print all the properties of this object
        '''
        for prop in self.__dict__:
            if not prop.startswith('_'):
                print(prop)
    @classmethod
    def __createMo__(cls,nxHandle,**options):
        '''
        Create new instances of the class using the nxHandle to send cli commands
        defined within the cls.__nxApi__(**options) method
        
        '''
        mos = []
        for cmd in cls.__nxApi__(**options):
            response = nxHandle.sendCmd(cmd)
            if not response:
                continue
            parser = importlib.import_module(cls.__parserModule__())
            mos.extend(parser.createMo(response))

        return mos
    
    def __fetchChildren__(self,nxHandle):
        '''
        Fetch the children of this object using the nxHandle to send cli commands
        defined within the cls.__nxApi__(**options) method
        
        '''
        mos = []
        for md in self.__childModules__():
            mod = importlib.import_module(md[0])
            klass = getattr(mod, md[1])
            parentKey = md[2]
            options = {parentKey: getattr(self, parentKey)}
            mos.extend(klass.__createMo__(nxHandle,**options))
            
        for mo in mos:
            self.__addChild(mo)
        
        

