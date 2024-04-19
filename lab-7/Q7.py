import numpy as np
import random
class Polynomial:
    def __init__(self,coeff_vect=[]):
        self.coeff_vect = coeff_vect
    def __str__(self): #to print the coefficient of polynomials
        strings=["array of the polynomial are: \n"]
        for i in self.coeff_vect:
            strings.append(str(i))
        return " ".join([x for x in strings])
    # Evaluating the polynomial at a point and using getitem to get the value
    def __getitem__(self, item):
        return sum([(item ** i) * self.coeff_vect[i] for i in range(len(self.coeff_vect))])
    
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
        
    
    def derivative(self):  # derivative method
        derivative_list = []
        for i in range(1, len(self.coeff_vect)):
            # The derivative formula of the polynomial [x^n becomes x^(n-1)]
            derivative_list.append((i) * self.coeff_vect[i])
        return Polynomial(derivative_list)
    
    def get_coef(self):  #method to find the coeffecients of the polynomial
        co = []
        for i in self.coeff_vect:
            co.append(i)
        return co

    
 #Creating method for ABERTH's Method root finding
    def Aberth_method(self):
        
        # creating a polynomial out of the given array elemnts
        p = Polynomial(self.coeff_vect)
        coef = p.get_coef()
        degree = len(coef) - 1  # getting degree of the Polynomial
        
        # finding upper and lower bounds of roots to start Aberth method
        upper = 1 + 1 / abs(coef[-1]) * max(abs(coef[x]) for x in range(degree))
        lower = abs(coef[0]) / (abs(coef[0]) + max(abs(coef[x]) for x in range(1, degree + 1)))
        # randomly choosing lists of roots inside the bounds to start Aberth Method
        roots_list=[]
        for i in range(degree):
            r = random.uniform(lower, upper)
            theta = random.uniform(0, np.pi * 2)
            approx_root = complex(r * np.cos(theta), r* np.sin(theta)) #complex root
            roots_list.append(approx_root)    
        df=p.derivative() #derivative of the polynomial
        
        
        
        iter = 0 #approximating the roots by iterating Abeth's method maximum 10 times
        while iter <10:

            for i in range(len(roots_list)):
                    f_df_ratio = p[roots_list[i]] / df[roots_list[i]] #calculating f(Zk)/f'(Zk)
                    #Calculating OFFSET (Wk)
                    Wk =f_df_ratio / (1-(f_df_ratio*sum(1/(roots_list[i]-j) 
                                                        for j in (roots_list) if j !=roots_list[i])))
                    roots_list[i] -= Wk
                    
            iter += 1
            
        return roots_list
                 

def bisection(f, a, b):# bisection method to find out roots
    A = a
    B = b
    N = 10000
    for n in range(1, N + 1):
        mid = (A + B) / 2
        f_mid = f(mid)
        if f(A) * f_mid < 0:
            A = A
            B = mid
        elif f(B) * f_mid < 0:
            A = mid
    return (A + B) / 2

#adding a method for finding all roots of a continuous function f over [a,b]...
# using Aberth Method and Bisection Method   


def All_Roots(function, a, b):
    F= function  # the continuous function
    x0 = a
    xn = b
    x = np.linspace(x0, xn, num=5)
    y = [F(i) for i in x]
    pol = np.polyfit(x, y, len(x) - 1)  #getting a close polynomial for the continuous function
    p = Polynomial(list(pol))
    aberth_roots = p.Aberth_method()  # roots of the Polynomial using Aberth method

    # deleting the complex roots
    aberth_real_roots = []
    for i in aberth_roots:
        if round(i.imag, 10) == 0:
            aberth_real_roots.append(i.real)
    aberth_real_roots.sort()
    # finding new roots
    updated_roots = [x0]
    for i in range(len(aberth_real_roots)):
        if (i == len(aberth_real_roots) - 1):
            break
        updated_roots.append((aberth_real_roots[i] + aberth_real_roots[i + 1]) / 2)
    updated_roots.append(xn)
    RootsIn_btw_a_b = []
    # Using bisection to get the roots  in each sub Intervals
    for i in range(len(updated_roots) - 1):
        if (F(updated_roots[i]) * F(updated_roots[i + 1]) < 0):
            r = round(bisection(F, updated_roots[i], updated_roots[i + 1]), 10)
            RootsIn_btw_a_b.append(r)

    #checking if the roots are with in an error 10^(-3)   
    error_tolerance=0
    for r in RootsIn_btw_a_b:
        if function(r)>10**(-3):
            error_tolerance=1
    if len(RootsIn_btw_a_b) !=0 and error_tolerance==0:
        print("All roots are with in an error 10^-3")
        print("Roots within the interval[",a,b,"] are :\n",RootsIn_btw_a_b)
    elif len(RootsIn_btw_a_b) !=0 and error_tolerance==1: 
        print("All Roots are NOT with in an error 10^-3") 

    elif len(RootsIn_btw_a_b)==0:
        print("No roots exist in [",a,b,"]")
    

function=lambda x: np.sin(x)
a=-np.pi / 2              #interval [a,b]
b=4 * np.pi / 3
All_Roots(function,a,b )





