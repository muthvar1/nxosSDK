def common_parser(output,suffix):
    objectList = []
    Table = 'TABLE_' + suffix
    Row = 'ROW_' + suffix
    if isinstance(output[Table][Row],list):
        for object in output[Table][Row]:
            objectList.append(object)
    else:
        objectList.append(output[Table][Row])
    return objectList

def moParser(output,mo):
    '''
    Given an mo and an output nested dictionary, iterate through the output recursively
    and assign each key value pair as an attribute/property of the mo. If the key matches the prefix of TABLE_
    followed by a nested key of ROW_ then the value of that key is a list of dictionaries. 
    In this case create an attribute of the mo with the suffix of the TABLE_ key and assign the list of dictionaries as the value.
    for example:
    TABLE_vrf
        ROW_vrf
            vrf_name: testvrf
            vrf_id: 4
            vrf_state: Up
            rd:
    If attribute is a hyphenated word, then replace the hyphen with an underscore
    '''
    if isinstance(output,dict):
        for key,value in output.items():
            if isinstance(value,dict):
                if key.startswith('TABLE_'):
                    if isinstance(value['ROW_'+key[6:]],list):
                        if '-' in key[6:]:
                            undAttr = key[6:].replace('-','_')
                            mo._baseMo__addAttr(undAttr,[])
                            for item in value['ROW_'+key[6:]]:
                                getattr(mo,undAttr).append(item)
                        else:
                            mo._baseMo__addAttr(key[6:],[])
                            for item in value['ROW_'+key[6:]]:
                                getattr(mo,key[6:]).append(item)
                    else:
                        moParser(value['ROW_'+key[6:]],mo)
                else:
                    moParser(value,mo)
            elif isinstance(value,list):
                if '-' in key:
                    undAttr = key.replace('-','_')
                    mo._baseMo__addAttr(undAttr,[])
                    for item in value:
                        getattr(mo,undAttr).append(item)
                else:
                    mo._baseMo__addAttr(key,[])
                    for item in value:
                        getattr(mo,key).append(item)     
            else:
                if '-' in key:
                    undAttr = key.replace('-','_')
                    mo._baseMo__addAttr(undAttr,value)
                else:
                    mo._baseMo__addAttr(key,value)
                
    




