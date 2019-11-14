num=int(input("Enter a number:"))
factors=[]
for i in range(1,num+1):
    if num%i== 0:
        factors.append(i)
print(factors)
if len(factors)==2:
    print("Its a prime")
else:
    print("Its not a prime")