import numpy as np
from matplotlib import pyplot as plt
import matplotlib.animation as Anim

h=0.25 #spatial step size
k=0.25 # time step size
T=2 #total time of simulation
x=np.arange(0,1+h,h)
t=np.arange(0,T+k,k)
n=len(x)
m=len(t)
U=np.zeros((n,m)) #initializing solution matix

#setting boundary and initial condition
BoundaryCond=[0,0]
InitialCond=np.e**(-x)
U[0,:]=BoundaryCond[0]  
U[-1,:]=BoundaryCond[1]
U[:,0]=InitialCond

#updating the Heat solution matrix
for j in range(1,m):
    for i in range(1,n-1):
        U[i,j]=(k/h**2)*U[i-1,j-1]+(1-2*(k/h**2))*U[i,j-1]+(k/h**2)*U[i+1,j-1]

U=U.round(3) #rounding off upto 3 decimal places 
print(U)

#plotting and animation
fig,ax=plt.subplots()
line,=ax.plot(x,U[:,0], color='red')
def animate(i):
    line.set_ydata(U[:,i])
    return line,
anim=Anim.FuncAnimation(fig,animate, frames=m,interval=50, blit=True)
plt.xlabel('Length of Rod')
plt.ylabel('Temperature')
plt.title('Heat Conduction')
plt.show()

