list=input("Enter the sentence").split()
new_list=[]
for word in list:
    new_list.append(word[::-1])
for word in new_list:
    print(word,end=" ")