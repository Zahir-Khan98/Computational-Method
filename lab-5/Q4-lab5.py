import math
from matplotlib import pyplot as plt
import numpy as np
from scipy import integrate
class Polynomial:
    def __init__(self,coeff_vect=[]):
        self.coeff_vect = coeff_vect
    def __str__(self): #to print the coefficient of polynomials
        strings=["Coefficients of the required Legendre polynomial are: \n"]
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

    #creating function to find out n -degree( take as argument) legendre polynomial (coefficients)
    def LegendrePolynomial(self,degree):
        p = Polynomial([-1, 0, 1]) # defining (x^2-1)
        pol = Polynomial([1]) #it simply means the constant "1" in the form of polynomial
    # Multiplying the polynomial n times
        for i in range(degree):
            pol = pol * p
    # differentiating (X^2 -1)^n  n-times
        for i in range(degree):
            pol = pol.derivative()
        legen_pol = (1 / ((2 ** degree) * math.factorial(degree))) * pol #calculating required legendre polynomial
        return legen_pol
    # to get the legendre pol: in the form of x (e.g, for legen_pol=[a0,a1,a2] we'll get a0+a1*x+a2*x^2)
    def legendre_Pol_Function(self, x):
        l = 0
        for i in range(len(self.coeff_vect)):
            l += (x ** i) * self.coeff_vect[i]
        return l
    def legend_approximation(self, degree): # the method to approximate using nth degree legendre polynomial
        p = Polynomial()
        legendre_coeff =[]
        for i in range(degree+1):
            legendre_coeff.append(p.LegendrePolynomial(i))  #getting legendre pol: co-effs of degree i
        Ck_values=[]  #creating an empty list for storing Ck values for k=0,1,..,n(=degree)  
        for k in range(degree+1):
            #calculating 'L_k(x)' and 'e^x.L_k(x)'
            Lk_sqr = lambda x: (legendre_coeff[k].legendre_Pol_Function(x))**2
            exp_Lk = lambda x: np.exp(x)*legendre_coeff[k].legendre_Pol_Function(x)
            #calculating C_k values:
            Ck =(list(integrate.quad(exp_Lk, -1, 1))[0])/(list(integrate.quad(Lk_sqr, -1, 1))[0])
            Ck_values.append(Ck)
        X = np.linspace(-1, 1, num=100) #Creating X- values for plotting by dividing the interval [-1,1] into 100 points

        #calculating the pol: approximation of e^x in the form of "Summation(Ck.Lk(x))" at X=a for k=0,..,n-1 
        #and storing the values in the list "Y" for each value of x=a in X
        Y =[]
        for a in X:
            Ck_Lk =0    
            for k in range(degree):
                Ck_Lk = Ck_Lk + Ck_values[k]*legendre_coeff[k].legendre_Pol_Function(a) #calculating Ck.Lk(a)
            Y.append(Ck_Lk)    
        #calculating values of e^x at x=a in X and storing that in X
        Y1=[np.exp(a) for a in X]    

        #plotting of visulisation of actual function e^x and approximated polynomia(using legendre function)
        fig,ax=plt.subplots()
        ax.plot(X, Y1,"yo",label="Actual $e^x$")
        ax.plot(X, Y,"r", label="Approximated polynomial of $e^x$ using Legendre function")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_title("plot Approximation Pol: of $e^x$ and actual plot of $e^x$")
        plt.grid(True, which="both")
        ax.legend()
        plt.show()
p=Polynomial()        
p.legend_approximation(10)             




    