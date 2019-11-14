def isSquare(num):
    if int(num**0.5)==(num**0.5):
        return True
    else:
        return False
    
def even(num):
    if num%2 == 0:
        return True
    else:
        return False
    
n=int(input("Enter number"))
for i in range(n):
    if isSquare(i) and even(i):
        print(i)
    else:
        pass