import scipy.integrate
import numpy as np
from matplotlib import pyplot as plt
#foll: below lists are for diffrent integration methods values for each subinterval
trapz_list=[] #for trapezoidal
simps_list=[]  #for simpson's
quad_list=[] #for quadrature
exact_list=[] #exact or actual value
# function we nned to find the area under
f= lambda x: 2*x*np.exp(x**2)
u=np.linspace(0,5,50) # divide the interval (0,2) into sub-intervals  (0,u)
for i in range(1,len(u)):
   I_quad=scipy.integrate.quad(f,0,u[i])
   x=np.linspace(0,u[i],10) #creating 50 x-values for each subintervals [0,u[i]]
   y=f(x)
   I_trapz=scipy.integrate.trapz(y,x)
   I_simps=scipy.integrate.simps(y,x)
   exact_list.append(np.exp(u[i]**2)-np.exp(1)) # actual value of the integration
   trapz_list.append(I_trapz) # trapezoidal approximation
   simps_list.append(I_simps) # simpson's approximation
   quad_list.append(I_quad[0]) # Quadrature rule
x=[u[i] for i in range(1,len(u))] # for each interval creating a x-value.
# plotting for visulization 
fig,ax=plt.subplots()
ax.plot(x,simps_list,"y",label="Simpson's")
ax.plot(x,quad_list,"r",label="Quadrature")
ax.plot(x,trapz_list,"b",label="Trapezoidal")
ax.plot(x,exact_list,"g--",label="Actual value")
ax.legend()
ax.set_xlabel("x-values (for each subintervals endpoint)")
ax.set_ylabel("Value of the integrations")
plt.grid(True,which="both")
ax.set_title("Visulization of different Numerical integration methods in scipy for the function 2x·e^x^2")
plt.show()