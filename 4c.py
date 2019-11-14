num=[]
n=int(input("Enter the number of values"))
for i in range(n):
    val=int(input("Enter value:"))
    num.append(val)
e_count,o_count=0,0
for ele in num:
    if ele %2 ==0:
        e_count+=1
    else:
        o_count+=1
print(e_count," ",o_count)