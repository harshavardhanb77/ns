def highest(names,marks):
    if(len(marks)==len(names)):
        maxMark=max(marks)
        index=marks.index(maxMark)
        maxName=names[index]
        return(maxName,maxMark)
        
names=[]
marks=[]
n=int(input("Enter the number of students"))
for i in range(n):
    names.append(input("name"))
    marks.append(int(input("Marks")))
    
print(highest(names,marks))