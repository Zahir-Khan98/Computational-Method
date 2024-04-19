import random
import numpy as np
from matplotlib import pyplot as plt
class RowVectorFloat:
    def __init__(self,vector=[]):
        self.vector=vector
     #overloading "__str__"  
    def __str__(self):  #to print the vector  elements (keys)
        string=" ".join([str(x) for x in self.vector])
        return "".join(string)
    #overloading "__len__"
    def __len__(self): #to get the length of the vctor
         return len(self.vector)
     #overloading "__getitem__"
    def __getitem__(self, i): #to get the ith vector element(key)
        return self.vector[i]   
     #overloading "__setitem__"
    def __setitem__(self,i,a): #to change i-th element(key) of vector to "a"
        self.vector[i]=a
        return self.vector[i]  
    def __add__(self, vector2): #overloading "add" operator for adding two vectors
        for i in range(len(self.vector)):
            self.vector[i]=self.vector[i]+vector2.vector[i]
        return self
    #overloading "__mul__" operator
    def __mul__(self,scalar):  #for operation like "2*[1,2,3]"
         return RowVectorFloat([x * scalar for x in self.vector])
         #as an instance of the class is on the right-hand side of the 
         # multiplication operator (*) and the other operand is a scalar,
         #so,we_have to use "__rmul__() which is similar as "__mul__" but for 
         # multiplication from right hand side 
    def __rmul__(self, scalar):
        return self * scalar  
  
class SquareMatrixFloat:
    def __init__(self, n): #size of matrix = n
        self.n = n
        self.matrix = [RowVectorFloat([0]*n) for i in range(n)]  
    
    def sampleSymmetric(self):
        for i in range(self.n): 
            for j in range(self.n):
                if i==j:
                    rand1 =round(random.uniform(2,self.n+1),2)  #setting diagonal element from (2,n), so that rows be
                    self.matrix[i][j] = rand1                                #diagonally dominant to get perfect visulisation
                elif i < j:    #setting non diagonal element
                    rand2 = round(random.random(),2)
                    self.matrix[i][j] = rand2
                    self.matrix[j][i] = rand2 
                    
        return self
    
    def isDRDominant(self):
        count = 0 #to count no. of diagonally dominant rows
        for i in range(self.n):
            if abs(self.matrix[i][i]) > abs(sum(self.matrix[i]) - self.matrix[i][i]):
                count = count +1
        if count == self.n: #if no. of diagonally dominant row = total no. of rows, then 
            return True                  #the matrix is "diagonally dominant" and "not" otherwise    
        else:
            return False 

    def jSolve(self, b,no_iter):
        self.b = b
        self.no_iter = no_iter
        jacobi_err_list =[]
        X = [0]*self.n   #initializong the soln as [0,0,...,0]   
        x_pre = [0]*self.n
        count=0 #for counting the no. of iteration
        while(count != no_iter): 
            for i in range(self.n): #in this loop, calculating the value of i-th variable 'Xi' in each iteration
                v=0                                            #and updating the value
                for j in range(self.n):
                    if j!=i:
                        v = v + self.matrix[i][j]*x_pre[j]
                X[i] = (self.b[i]-v)/self.matrix[i][i] #updating "Xi" value
            jacobi_err_list.append(np.linalg.norm(np.dot(self.matrix,X)-self.b)) #calculating ||AX-b|| to find the error  
            x_pre = [X[i] for i in range(self.n)]                             #in "count"= k-th iteration
            count = count+1                                                                    
        return jacobi_err_list 
    
    def gsSolve(self,b,no_iter):
        self.b=b
        self.no_iter = no_iter      
        seidal_err_list =[]
        X = [0]*self.n   #initializong the soln as [0,0,...,0]   
        count=0 #for counting the no. of iteration
        while(count != no_iter): 
            for i in range(self.n): #in this loop, calculating the value of i-th variable 'Xi' in each iteration
                v=0                                            #and updating the value
                for j in range(self.n):
                    if j !=i:
                        v = v + self.matrix[i][j]*X[j]   
                X[i] = (self.b[i]-v)/self.matrix[i][i] #updating "Xi" value instantly, as we are following gauss seidal
            seidal_err_list.append(np.linalg.norm(np.dot(self.matrix,X)-self.b)) #calculating ||AX-b|| to find the error  
            count=count+1                                                                       #in "count"= k-th iteration
        return seidal_err_list
    def seidal_jacobi_rateOFconvergance(self,b,no_iter):
        self.b=b  #column vector "b" in linear system of equation "AX = b"
        self.no_iter=no_iter #number of iteration
        x=[i for i in range(1,self.no_iter+1)] #defining X-axis values
        Y_jacobiError = self.jSolve(b,no_iter)
        Y_seidalError = self.gsSolve(b,no_iter)
        plt.xlabel("Number of Iteration")
        plt.ylabel("Rate of Convergance (towards X-axis)")
        plt.plot(x,Y_jacobiError , c = "b", label="Jacobi Method")
        plt.plot(x,Y_seidalError , c = "g", label="seidal Method")
        plt.legend()
        plt.grid()
        plt.show()

s = SquareMatrixFloat(4)
s.sampleSymmetric()
s.seidal_jacobi_rateOFconvergance([1,2,3,4],50)

