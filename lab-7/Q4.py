import numpy as np
from matplotlib import pyplot as plt


def Visualize_NR_vs_Secant_convergance(f,df_dx,eps):
    
    #calculating iterated points for Newton raphson
    x0=1
    function_vals_of_NR=[] #initialization of iterated value of Newton Raphson method with a empty list
    iteration_count_NR=[]
    i=0
    while abs(f(x0))>eps:
        x_next=x0-f(x0)/df_dx(x0)
        function_vals_of_NR.append(f(x_next))
        x0=x_next
        i=i+1
        iteration_count_NR.append(i)
    
    #calculating iterated points for secant method
    x0=0
    x1=2
    function_vals_of_Secant=[] #initialization of iterated value of secant method with a empty list
    iteration_count_Secant=[]
    j=0
    while abs(f(x1))>eps:
        if (f(x1)-f(x0)) !=0:
            x_next2 =x1-(f(x1)*(x1-x0))/(f(x1)-f(x0)) 
            function_vals_of_Secant.append(f(x_next2))
            x0=x1
            x1=x_next2
            j=j+1
            iteration_count_Secant.append(j)

    #plotting for visulizing the rate of convergance   
    fig, ax = plt.subplots()
    ax.plot(iteration_count_NR, function_vals_of_NR, "r-", label="Newton raphson")
    ax.plot(iteration_count_Secant, function_vals_of_Secant, "b-", label="Secant Method")
    ax.grid()
    ax.legend()
    ax.set_xlabel("No of iterations")
    ax.set_ylabel("Functional Values")
    ax.set_title("Visualization of Convergence of Newton-Raphson vs Secant Method", fontsize=10)
    plt.show()
   
# Defining the function x^2 + sin(x) - 2
def f(x):
    return x**2 + np.sin(x) - 2
    #return x - np.cos(x)
    

# Defining the derivative of the function
def df_dx(x):
    return 2*x + np.cos(x)
    #return 1 + np.sin(x)
    

Visualize_NR_vs_Secant_convergance(f,df_dx,eps=10 ** (-10))
