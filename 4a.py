import cmath
a=int(input("Enter the value of a"))
b=int(input("Enter the value of b"))
c=int(input("Enter the value of c"))
d=((b**2)-(4*a*c))
if d == 0:
    print("Roots are equal")
elif d>0:
    print("Roots are real and not equal")
else:
    print("Roots are imaginary")
r1=(-b + cmath.sqrt(d))/2*a
r2=(-b - cmath.sqrt(d))/2*a
print("Roots ",r1," and ",r2)