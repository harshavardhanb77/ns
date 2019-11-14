#Check whether given number is part of fibbonnaci number
num=int(input("Enter the number:"))
first=0
second=1
if num == first:
    print("The number is fib series")
elif num == second:
    print("The number is in fib series")
else:
    flag=0
    third=first+second
    while(third<=num):
        if third == num:
            flag=1
        first=second
        second=third
        third=first+second
    if flag == 1:
        print("The number is in fib series")
    else:
        print("The number is not in fib")
        
    