with open("text1.txt","r") as f1,open('text1a.txt','r') as f2:
    for i,j in zip(f1,f2):
        if set(i.split()) == set(j.split()):
            print(i.strip())
        else:
            print(i.split(),j.split())
            
with open("text1.txt","r") as f1,open('text1a.txt','r') as f2:            
    for i,j in zip(f1,f2):
        if set(i.split()) == set(j.split()):
            print(i.strip())
        else:
            pass
        
with open("text1.txt","r") as f1,open('text1a.txt','r') as f2:            
    for i,j in zip(f1,f2):
        if set(i.split())== set(j.split()):
            pass
        else:
            print(j.strip())
            
            
with open("text1.txt","r") as f1,open('text1a.txt','r') as f2:            
    for i,j in zip(f1,f2):
        if set(i.split())== set(j.split()):
            pass
        else:
            print(i.strip(),j.strip())

        