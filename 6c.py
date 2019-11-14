list=input("ENter the sentence").split()
count=0
new=[]
for word in list:
    if(len(word)>2 and word[0]==word[-1]):
        count+=1
        new.append(word)
print(count)
print(new)
        