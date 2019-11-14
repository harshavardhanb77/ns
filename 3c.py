a,b=(input("Enter the two operands:")).split()
a=int(a)
b=int(b)
t=a
a=b
b=t
print("After swapping",a," ",b)
#Without third variable
a=a+b
b=a-b
a=a-b
print("After swapping",a," ",b)