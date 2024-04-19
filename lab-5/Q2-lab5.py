from scipy import integrate
from matplotlib import pyplot as plt
import numpy as np
class Polynomial:
    def __init__(self,coeff_vect=[]):
        self.coeff_vect = coeff_vect
    def __str__(self): #to print the coefficient of polynomials
        strings=["Coefficients of the Best fit polynomial are: \n"]
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
        return "Area in the interval " + str([self.a, self.b]) + " is: " + str((p[self.b] - p[self.a]))


# least square  polynomial for a given function
def Best_Fit_Polynomial(degree):
    co_list = [] #for list of row of coefficient matrix
    #calculating Coefficients of a_k's in LHS of Normal Equation (given in slide)
    for j in range(degree+1):
        j_th_row =[] # j-th row of A, in the system of linear equation AX=b 
        for k in range(degree+1):
            j_k_th_elems=[]
            s = lambda x: x ** (j+k) #calculating X^(j+k)
            j_k_th_elems= list(integrate.quad(s, 0, np.pi))[0] #calculating j-k th element of coeff_matrix by integrating term wise
            j_th_row.append(j_k_th_elems)
        co_list.append(j_th_row) 
    b = [] #column vector for Ax=b
    for j in range(degree+1):
        s = lambda x: (x ** j) * (np.sin(x) + np.cos(x)) #calculating
        b.append(list(integrate.quad(s, 0, np.pi))[0])
    A = np.array(co_list) # co-effecient matrix 
    B = np.array(b) # RHS of the linear system of equation
    sol = np.linalg.solve(A, B) # solution of the linear equation Ax=B

    a = 0  
    b = np.pi

    x = np.linspace(a, b, num=20) #creating x-values for plotting
    # setting up a polynomial object to valuate a value at points and
    # using it in a plot
    p = Polynomial(sol) # creating the polynomial object
    y1 = [p[i] for i in x] #values of approximated polynomial corresponding to x values.
    y2 = [np.sin(i) + np.cos(i) for i in x] #values of actual function corresponding to x-values
    fig, ax = plt.subplots()

    ax.plot(x, y2, "yo", label="Actual function : $sin(x)+cos(x)$")
    ax.plot(x, y1,"r", label="Approximated Polynomial function")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Plot of approximated polynomial and actual function:  $sin(x)+cos(x)$",fontsize=10)
    plt.grid(True, which="both")
    print(p)
    ax.legend()
    plt.show()

Best_Fit_Polynomial(10)