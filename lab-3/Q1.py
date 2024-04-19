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
    #overloading "__add__" operator
    def __add__(self, vector2): #overloading "add" operator for adding two vectors
        for i in range(len(self.vector)):
            self.vector[i]=self.vector[i]+vector2.vector[i]
        return self

    #overloading "__mul__" operator     
    def __rmul__(self, scalar):
        return RowVectorFloat([x * scalar for x in self.vector]) #for operation like "2*[1,2,3]"
     
#r= RowVectorFloat([1,2,3])
#print(r)
#r= RowVectorFloat([1,2,3])
#print(len(r))  
#r= RowVectorFloat([1,2,4])
#print(r[1]) 
r1 = RowVectorFloat([1, 2 , 4])
r2 = RowVectorFloat([1, 1 , 1])
r3 = 2*r1 + (-3)*r2
print(r3)    