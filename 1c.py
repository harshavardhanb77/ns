import math
a=float(input("Enter the value of side A"))
b=float(input("Enter the value of side B"))
c=float(input("Enter the value of side C"))
s=(a+b+c)/2
s=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("area is",s)