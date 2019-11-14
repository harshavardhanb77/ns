
num=int(input("Enter the number of values"))
list=[]
for i in range(num):
    list.append(int(input("ENter the number")))
dicte={}
for ele in list:
    dicte[ele]=0
for ele in list:
    dicte[ele]+=1
val=dicte.values()
max_value=max(val)
for ele in dicte.keys():
    if dicte[ele] == max_value:
        mode=ele
print('mode=',mode)