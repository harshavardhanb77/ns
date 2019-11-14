num=int(input("Enter the number"))
i=1
sum=0
for i in range(1,num):
    if(num%i==0):
        sum+=i
if(sum== num):
    print("The number is perfect number")
else:
    print("Not perfect")