x={'apple':'fruit','cat':'mammal','dog':'mammal','banana':'fruit','Carrot'
   :'veg'}

def mod(d):
    dicta={}    
    for item in d:        
        if d[item] not in dicta:
            print(d[item])
            dicta[d[item]]=[]
            dicta[d[item]].append(item)
        else:
            dicta[d[item]].append(item)
    return dicta    
        
print(mod(x))