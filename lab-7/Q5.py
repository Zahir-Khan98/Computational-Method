import numpy as np
from matplotlib import pyplot as plt
def Newton_Raphson(f, Jacobi_of_f, x0, no_of_iteration):
    Xk_vals = [x0]  # list of values(x0,x1,x2,.....) of successive approximations in iterations
    x = x0
    #iterations of newton raphsons      
    for _ in range(no_of_iteration):
#formula for newton-raphson for vector valued function is x_k+1= x_k -J(x_k)^{-1}*F(x_K); where J is jacobian of F
        x = x - np.linalg.inv(Jacobi_of_f(x)) @ f(x) #The symbol "@" is generally used for matrix multiplication
        Xk_vals.append(x)
    return Xk_vals

def f(x): #defining the given input function f
    x1, x2, x3 = x
    f1 = 3 * x1 - np.cos(x2 * x3) - (3 / 2)
    f2 = 4 * (x1**2) - 625 * (x2**2) + 2 * x3 - 1
    f3 = 20 * x3 + np.exp(-1 * x1 * x2) + 9
    return [f1, f2, f3]

def Jacobi_of_f(x): #finding the jacobian of f
    x1, x2, x3 = x
    J1 = [3, x3 * np.sin(x2 * x3), x2 * np.sin(x2 * x3)]
    J2 = [8 * x1, -1250 * x2, 2]
    J3 = [-x2 * np.exp(-1 * x1 * x2), -x1 * np.exp(-1 * x1 * x2), 20]
    return [J1, J2, J3]
  
x_vals_NR = Newton_Raphson(f,Jacobi_of_f, x0=[1, 2, 3], no_of_iteration=50) #performing Newton Raphson

print(f"The root of the function is {x_vals_NR[-1]}") #last iterated root has been taken as root

f_X_k = [np.linalg.norm(f(x)) for x in x_vals_NR]  #Evaluating ||f(X_k)|| values at the obtained points X_k s

# Plotting 
plt.title("k-th Iterations of Newton_Raphson AGAINST value of ||f(X_k)||")
plt.xlabel("Iteration")
plt.ylabel("||f(X_k)||")
plt.plot(list(range(0, len(x_vals_NR))), f_X_k,'r--', label="(k,||f(X_k)||)")
plt.legend()
plt.grid()
plt.show()