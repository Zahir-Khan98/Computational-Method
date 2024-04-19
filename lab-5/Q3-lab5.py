import math
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
def LegendrePolynomial(degree):
    p = Polynomial([-1, 0, 1]) # defining (x^2-1)
    pol = Polynomial([1]) #it simply means the constant "1" in the form of polynomial
    # Multiplying the polynomial n times
    for i in range(degree):
        pol = pol * p
    # differentiating (X^2 -1)^n  n-times
    for i in range(degree):
        pol = pol.derivative()
    legen_pol = (1 / ((2 ** degree) * math.factorial(degree))) * pol #calculating required legendre polynomial
    print(legen_pol)

LegendrePolynomial(5)

    