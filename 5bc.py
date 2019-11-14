i,flag=1,0
num=int(input("Enter the number:"))
while(2**i<=num):
    if(2**i == num):
        flag=1
    i+=1
if flag == 0:
    print("The number is not power of two")
else:
    print("The number is power of two")