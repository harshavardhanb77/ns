n=int(input("ENter number of students"))
s,p,c,m,b=[],[],[],[],[]
for i in range(n):
    s.append(input("Enter usn"))
    p.append(int(input("P marks")))
    c.append(int(input("C marks")))
    m.append(int(input("M marks")))
    b.append(int(input("B marks")))

usnDict={}
for i in range(n):
    usnDict[s[i]]=[p[i],c[i],m[i],b[i]]

print(usnDict)

mark={}
for i in range(n):
    mark[s[i]]=p[i]+c[i]+m[i]+b[i]
    
for i,j in sorted(mark.items(),key=lambda a:a[1],reverse=True):
    print(i," ",j)

student={}
for i in range(n):
    student[m[i]]=[]

for i in range(n):
    student[m[i]].append(s[i])
    
print(student)