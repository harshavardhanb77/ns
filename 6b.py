string=input("Enter the string")
c=0
d=0
s=0
for char in string:
    if(char.isalpha()):
        c+=1
    elif(char.isdigit()):
        d+=1
    elif(char != ''):
        s+=1
print(c," ",d," ",s)
        