import math
from scipy import integrate 
class Polynomial:
    def __init__(self,coeff_vect=[]):
        self.coeff_vect = coeff_vect
    def __str__(self): #to print the coefficient of polynomials
        strings=["Coefficients of the required Chebyshev polynomial are: \n"]
        for i in self.coeff_vect:
            strings.append(str(i))
        return " ".join([x for x in strings])
    
     #overloading "__add__" operator
    def __add__(self, other): # for adding two polynomial
        if len(self.coeff_vect) > len(other.coeff_vect): #incase if degree(pol1) > degree(pol2)
            for i in range( len(self.coeff_vect) - len(other.coeff_vect)):
                other.coeff_vect.append(0)                            
        if len(self.coeff_vect) < len(other.coeff_vect): #incase if degree(pol1) < degree(pol2)
            for i in range(len(other.coeff_vect)- len(self.coeff_vect)):
                self.coeff_vect.append(0)        

        for i in range(len(self.coeff_vect)):
            self.coeff_vect[i]=self.coeff_vect[i] + other.coeff_vect[i]
        return self
    #overloading "__sub__" (substraction) operator 
    def __sub__(self, other): # for substracting one polynomial from another
        if len(self.coeff_vect) > len(other.coeff_vect): #incase if degree(pol1) > degree(pol2)
            for i in range( len(self.coeff_vect) - len(other.coeff_vect)):
                other.coeff_vect.append(0)                            
        if len(self.coeff_vect) < len(other.coeff_vect): #incase if degree(pol1) < degree(pol2)
            for i in range(len(other.coeff_vect)- len(self.coeff_vect)):
                self.coeff_vect.append(0)
        for i in range(len(self.coeff_vect)):
            self.coeff_vect[i] = self.coeff_vect[i] - other.coeff_vect[i]
        return self
    
     #overloading "__mul__" operator
    def __mul__(self,other):
        #for operation like "polynomial1*polynomial2"
        pol_prod=[0]*(len(self.coeff_vect)+len(other.coeff_vect)-1)
        for i in range(len(self.coeff_vect)):
            for j in range(len(other.coeff_vect)):
                    #the pol: product coefficient list (p3) length = sum of the lengths of
                    #the two pol: lists minus one, as the highest degree 
                    #term in the result will have degree len(p1) + len(p2) - 1.
                pol_prod[i+j]+=self.coeff_vect[i]*other.coeff_vect[j]
        self.coeff_vect = pol_prod        
        return self
    def __rmul__(self, other):
        #for operation like "2*[1,2,3]"
        result=[x * other for x in self.coeff_vect]
        self.coeff_vect=result   
        return self
        
    #finding the value of polynomial at a point x, using "getitem"
    def __getitem__(self, x):
        return sum([(x ** i) * self.coeff_vect[i] for i in range(len(self.coeff_vect))])
    
    def derivative(self):  # derivative method
        derivative_list = []
        for i in range(1, len(self.coeff_vect)):
            # The derivative formula of the polynomial [x^n becomes x^(n-1)]
            derivative_list.append((i) * self.coeff_vect[i])
        self.coeff_vect = derivative_list
        return self

    # creating function to find the n th  chebyshev polynomial using recurrence relation
    def Chebyshev_Polynomial(self,degree):
        T_0 = Polynomial([1]) # 0-th ch: polynomial "T_0(x)=1"
        T_1 = Polynomial([0, 1]) # 1-st ch: polynomial "T_1(x)=x"
        i = 1
        # recursive calculation for chebyshev's polynomial with T_(n+1)(x)=2T_n(x) - T_(n-1)(x)
        while i < degree:
            p = 2 * Polynomial([0, 1]) * T_1 - T_0
            T_0 = T_1
            T_1 = p
            i += 1
        if degree == 0:
            return T_0
        elif degree == 1:
            return T_1
        else:
            return p
    # to get the chebyshev polynomial in the form of x (e.g, for p=[a0,a1,a2], we'll get a0+a_1.x+ a_2.x^2)
    def Chebyshev_Pol_Fn(self, x):
        s = 0
        for i in range(len(self.coeff_vect)):
            s = s + (x ** i) * self.coeff_vect[i]
        return s   
    def Print_firstFive_Chebyshev_pols(self): #to print 1st 5 chebyshev pol:
        chebyshev_coeff = []
        p = Polynomial()
        print("Printing first 5 Chebyshev polynomials \n")
        for i in range(5):
            #chebyshev_coeff.append(p.Chebyshev_Polynomial(i)) 
            print("The coefficients of ",i,"-th degree Chebyshev polynomial is: ",p.Chebyshev_Polynomial(i))   
     # function to check orthogonality of the first chebyshev polynomial
    def Orthogonality(self):
        chebyshev_coeff = []
        p = Polynomial()
        for i in range(5):
            chebyshev_coeff.append(p.Chebyshev_Polynomial(i)) # storing the first 5 chebyshev polynomials    
        # Checking of orthogonality
        v=[]
        for i in range(5):
            for j in range(5):
                    if i<j:                 #taken this kind of condition to avoid repetition.
                                     #(e.g- {i=2,j=4} and {i=4,j=2} --to avoid this type of repetition)
                    # taking the product with the weight function w(x)=1/sqrt(1-x^2)
                        s = lambda x: chebyshev_coeff[i].Chebyshev_Pol_Fn(x) * chebyshev_coeff[j].Chebyshev_Pol_Fn(x) * 1 / math.sqrt(1 - x ** 2)
                        int_val = integrate.quad(s, -1, 1)
                        v.append(int_val[0])
                        print("Intrgration of", i, "deg: chebyshev Pol: and", j, "deg: chebyshev Pol: along with weight function w(x) is : \n",
                           round(abs(int_val[0]), 8))
            #if The chebyshev pol: are Orthogonal then return "ORTHOGONAL" and if not then return "NOT ORTHOGONAL"
        print("\n")    
        if round(sum(v),4) ==0.0:
            print("ORTHOGONAL")    
        else:
            print("NOT ORTHOGONAL") 
                       
p=Polynomial() 
p.Orthogonality() #to write integration values and to print "ORTHOGONAL" Or "NOT ORTHOGONAL"
p.Print_firstFive_Chebyshev_pols() #to print first five Cheb: pol:
    