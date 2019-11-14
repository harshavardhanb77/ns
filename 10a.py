class Matrix:
    def __init__(self,row,col):
        self.row=row
        self.col=col
        self.matrix=[[0 for j in range(col)]for i in range(row)]
        
        
    def populate(self,name):
        print("Populating matrix"+name)
        for i in range(self.row):
            for j in range(self.col):
                self.matrix[i][j]=int(input("enter value:"))
            print("")
            
    def read(self,name):
        print("Printing matrix"+name)
        for i in range(self.row):
            for j in range(self.col):
                print(self.matrix[i][j])
            print("")
    
    def add(self,name,MatrixB):
        if self.row == MatrixB.row and self.col == MatrixB.col:
            for i in range(self.row):
                for j in range(self.col):
                    self.matrix[i][j]+=MatrixB.matrix[i][j]
        else:
            print("Invalid dimension")
        self.read(name)
        
MatrixA=Matrix(2,2)
MatrixA.populate("MatA")

MatrixB=Matrix(2,2)
MatrixB.populate("MatB")
MatrixA.add("MatA",MatrixB)
            
            
            
            
         
        