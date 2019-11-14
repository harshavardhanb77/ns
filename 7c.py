num=int(input("Enter the number of values"))
list=[]
for i in range(num):
    list.append(int(input("ENter the number")))
sum=0
for numb in list:
    sum+=numb
mean=sum/num
for numb in list:
    s=(numb-mean)**2
    sd=(s/num)**0.5
print(sd," ",mean)