import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as Animation

def visualize_heat_conduction(xc, yc, T, dt, dx):
    # T: total time to simulate
    # dt: time step for numerical integration
    # dx: spatial step for numerical integration
    
    # Define the grid
    x = np.arange(0, 1 + dx, dx)
    y = np.arange(0, 1 + dx, dx)

    # Define the initial condition
    u = np.zeros((len(x),len(y)))
    # Apply the boundary condition
    u[0, :] = u[-1, :] = u[:, 0] = u[:, -1] = 0
    # Define the heat source function
    def f(x, y, t):
        return np.exp(-np.sqrt((x - xc)**2 + (y - yc)**2))
    
    #plotting and updating
    fig=plt.figure()
    ims=[]
    # Define the numerical scheme
    alpha = dt / dx**2
    # Update the temperature
    for t in np.arange(0, T, dt):
        for i in range(1,len(x)-1):
            for j in range(1,len(x)-1):
                u[i,j] +=alpha*(u[i+1,j]-2*u[i,j]+u[i-1,j])
                u[i,j] +=alpha*(u[i,j+1]-2*u[i,j]+u[i,j-1])
                u[i,j] +=dt*f(x[i],y[j],t*dt)
               
        im=plt.imshow(u,cmap='hot',origin='lower',animated=True)  
        ims.append([im])  
    Anim=Animation.ArtistAnimation(fig,ims,interval=40,blit=True)   
    plt.show()  
visualize_heat_conduction(xc=0.1, yc=0.1, T=1, dt=0.20, dx=0.10)
       