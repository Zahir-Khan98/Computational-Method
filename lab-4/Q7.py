from matplotlib import pyplot as plt
import numpy as np
import math
class Polynomial:
    def __init__(self,coeff_vect=[]):
        self.coeff_vect = coeff_vect
    def __str__(self): #to print the coefficient of polynomials
        strings=["Coefficients of the polynomial are: \n"]
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

    def area(self, a, b):  # area method
        self.a = a #lower limit of def: integral
        self.b = b #upper limit of def: integral
        # intilalizing the list of the co-efficients with a zero to compensate for the constant part
        Integration_list = [0]
        for i in range(len(self.coeff_vect)):
            # integration formula of a polynomial, recall- int(x^n)=x^n/n+1
            Integration_list.append(self.coeff_vect[i] / (i + 1))
        p = Polynomial(Integration_list)  # Creating a polynomial with the co-efficients
        v = (p[self.b] - p[self.a])
        return v
    
#since "integration(e^x.sinx) = (e^xsinx)/2", so value of avtual area will be as following below:
Exact_area= (np.exp(1/2)*np.sin(1/2) - np.exp(0)*np.sin(0))/2 
# Approximate the integration with taylor series polynomial
fn = lambda n: (2 ** (n / 2) * np.sin(n * np.pi / 4))/math.factorial(n)
approx_pol_coeff=[fn(0)] #in this list we'll append approximated pol: coeff: of e^x.sin(x)

for i in range(1,10): #checking the approximation upto 100 interation
    
    p=Polynomial(approx_pol_coeff)

    if abs(p.area(0,1/2)-Exact_area)>= 10**-6: #checking the approximation area error is less than 10^(-6) or not
        approx_pol_coeff.append(fn(i)) # if not, we'll append next coefficient
    else:  
            
        p=Polynomial(approx_pol_coeff)
        break   


error = abs(p.area(0,1/2)-Exact_area)
print("The approximated area is: ",p.area(0,1/2))
print("The approximation error is",error)
   
          
