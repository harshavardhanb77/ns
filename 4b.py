num=int(input("Enter the number"))
sum=0
for i in range(1,num+1):
    sum+=i
    if(i == num):
        print(i,end="=")
        print(sum)
    else:
        print(i,end="+")
prod=1

for i in range(1,num+1):
    prod*=i
    if(i == num):
        print(i,end="=")
        print(prod)
    else:
        print(i,end="*")