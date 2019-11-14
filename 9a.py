f=open("text.txt","r")
f1=open("text1.txt","w")

for i,j in enumerate(f.readlines(),1):#i=line no and j=string
    f1.write(str(i)+" "+j)

f1.close()
f.close()
    