import numpy as np
from matplotlib import pyplot as plt

#To Constructs a polynomial that passes through a given set of points, then evaluates the polynomial.
from  scipy.interpolate import barycentric_interpolate


# Method for calculating Euler forward method
def Euler_Forward_Method(h):
    #as our "Initial value condition" is - x(0)=5      
    t0=0 # intial value of t
    x0=5 # initial value of x
    sol_t=[]
    sol_x=[]
    f=lambda t,x: -2*x # for the ODE X'(t)=-2X(t)
   #Euler Formula
    while t0<=10:
        xn=x0+h*f(t0,x0) #calculating, x_n+1 = x_n + h*f(t_n,x_n)
        sol_t.append(t0)
        sol_x.append(x0)
        t0=t0+h #calculating t_n+1=t_n+h
        x0=xn
    return sol_t,sol_x


fig,ax=plt.subplots(5,figsize=(8,18),sharex=True)

f=lambda t: 5*np.exp(-2*t) #solution of the given ODE,x'(t)=-2x(t);x(0)=5
h=[0.1, 0.5, 1, 2, 3]
for i in range(len(h)):
 #using Euler forward method,calculating t values(t0,t1,t2,...) and corresponding x values (x0,x1,x2,...) from the given ODE,..
                                                       #x'(t)=-2x(t),with initial condition x(0)=5
        t = Euler_Forward_Method(h[i])[0]
        x = Euler_Forward_Method(h[i])[1]

        #exact_sol_x = [f(i) for i in t ] # exact values of x corresponding to t
        t_val = np.linspace(min(t), max(t),100)
        x_val = barycentric_interpolate(t, x, t_val) #By barycentric_interpolate , calculating x(t_val) using the data (tn,xn) 
        exact_sol_x = [f(i) for i in t_val ] # exact values of x corresponding to t
        ax[i].plot(t_val, x_val,label="Solution by Euler Method")
        ax[i].plot(t_val,exact_sol_x,label="Exact solution")
        ax[i].legend()
        ax[i].grid()
        ax[i].set_title("Forward Euler Method for step length "+str(h[i]),fontsize=10)


#tight_layout automatically adjusts subplot params so that the subplot(s) fits in to the figure area. 
fig.tight_layout(pad=4.0) #pad=4.0 means, there will be 4 units of gap between two plots to make visible the title

plt.show()