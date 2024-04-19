
from matplotlib import pyplot as plt
import numpy as np
import scipy.integrate as si

def ODE_sol(mu, x0, x1, t0, t1):
    
    #for solving the given ODE and evaluating the time period of the ODE.
    def van_der_pol_derivatives(t, y):
        # the system of ODE is , d/dt[x,v]^t = [v ,mu * (1 - x * x) * v - x]^t  ; where v = dx/dt 
        x, dx = y
        return [dx, mu * (1 - x * x) * dx - x] #the derivatives of the system of ODE
    #generating t= Time values for plotting 
    t = np.linspace(t0, t1, 500)

    # Solving the system of ODE s using solve_ivp, which gives solution for x(t),dx/dt corresponding to t
    sol = si.solve_ivp(fun=van_der_pol_derivatives, t_span=[t0, t1], y0=[x0, x1], t_eval=t)

    # Values of points on the curve         #sol.y[1] gives x'
    x_t = sol.y[0]

    # Plotting the curve t vs x(t)
    plt.title(f"Van der Pol equation for mu = {mu}")
    plt.xlabel("t")
    plt.ylabel("x(t)")
    plt.plot(t, x_t, 'r')
    plt.grid()
    plt.show()

    # finding the Time Period of limit cycle  
    l1 = 0
    for i in range(1,len(t)):    
        if x_t[i] <= 0 and x_t[i + 1] >= 0:
            l1 = i                            
            break

    l2 = 0
    for i in range(l1+1,len(t)):
        if x_t[i] <= 0 and x_t[i + 1] >= 0:
            l2 = i
            break

    # as time period of the osscilation =The time taken for one complete oscillation to occur
    #so time period is =|t(l1)-t(l2)|
    timePeriod = abs(t[l1] - t[l2])
    print(f"The time period of the limit cycle for mu = {mu} is {timePeriod}")

#ODE_sol(mu,x0, x1, t0, t1)   
ODE_sol(2,0,1,0,50)
