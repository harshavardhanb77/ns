s1=set(input("Enter the first set").split())
s2=set(input("Enter the second set").split())
for i in s1:
    for j in s2:
        print('<',int(i),",",int(j),">")