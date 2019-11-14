class Item:
    def __init__(self,name):
        self.name=name
        self.rate=int(input("Enter the amount"))
        self.quantity=int(input("Enter the quantity"))
        self.itemTotal=self.rate*self.quantity
        
    def display(self):
        print("The item name is"+self.name)
        print("The item rate is",self.rate)
        print("The item quatity is",self.quantity)
        print("The item total is",self.itemTotal)
        
    def quantityUpdate(self,extra):
        self.quantity+=extra
        
class Bill:
    def __init__(self,name,noProduct):
        self.name=name
        self.noProduct=noProduct
        self.items={}
        count=0
        while(count<noProduct):
            item=input("Enter the item name")
            if item in self.items:
                choice=input("Item already present.Go back Y/N")
                if(choice == 'Y' or choice == 'y'):
                    pass
                else:
                    choice=int(input("1.Overwrite 2.Add extra"))
                    if(choice == 1):
                        pass
                    elif(choice == 2):
                        extra=int(input("Enter the extra quantity"))
                        self.items[item].quantityUpdate(extra)
                    else:
                        print("Invalid choice")
            else:
                self.items[item]=Item(item)
            count+=1
            
        self.totalItem=0
        self.totAmt=0
        for item in self.items.keys():
            self.totAmt+=self.items[item].itemTotal
            self.totalItem+=self.items[item].quantity
            
            
    def Display(self):
            print("Cust name"+self.name)
            for i in (self.items.keys()):
                self.items[i].display()
  

cust=[]
n=int(input("Enter number of customers"))
for i in range(n):
    name=input("Enter the name")
    no=int(input("Enter the no of product"))
    cust.append(Bill(name,no))

print("-----------")
for i in cust:
    i.Display()      