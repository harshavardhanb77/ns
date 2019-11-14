i,flag=1,0
num=int(input("Enter the number"))
while(i**2<=num):
    if(i**2==num):
        flag=1
    i+=1
if flag==1:
    print("The number is perfect square")
else:
    print("The number is not a perfect square:")
        