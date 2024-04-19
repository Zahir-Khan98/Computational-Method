import math
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

def solveDEs(DEs, theta0, dTheta_dt0, h, t0, t_max):
    g=9.8 #g-value
    L=0.1 #length of the rod
    #initializing the given ODEs variable
    t = t0
    theta = theta0
    dTheta_dt = dTheta_dt0
    theta_list = [theta0]  # List to store theta values

    # Applying the forward Euler method to get the solution 
    while t <= t_max:
        fn = DEs(t, theta, dTheta_dt, g, L)
        theta = theta + h * fn[0]
        dTheta_dt = dTheta_dt + h * fn[1]
        theta_list.append(theta)
        t += h

    def bobs_position(a):
        
        #Return the (x, y) coordinates of the bob at angle 'a'
        
        return L * math.sin(a), -L * math.cos(a)

    # Figure and Axes of the plot
    fig = plt.figure()
    ax = fig.add_subplot(aspect="equal")

    # The initial position of the pendulum rod
    x0, y0 = bobs_position(theta0)
    line, = ax.plot([0, x0], [0, y0], lw=1, c="y")

    # The pendulum bob
    bob_radius = 0.008
    bob = ax.add_patch(plt.Circle(bobs_position(theta0), bob_radius, fc="g", zorder=3))
                              #'zorder' is used for avoiding overlapping two-dimensional objects

    # The pendulum rod (Patch)
    PENDULUM = [line, bob]

    def canvas():
        ax.set_title("Simple Gravity Pendulum Graphics")
        # Setting the plotting axes
        ax.set_xlim(-L * 2, L * 2)
        ax.set_ylim(-L * 2, L * 2)
        ax.plot([-0.05,0.05],[0,0],"k",linewidth=2) #Hanger of the pendulum
        # Return everything that must be plotted at the start of the animation
        return PENDULUM

    def dynamic_fig(i):  #creating animated dynamic frames of pendulum
        #suppose in 'FuncAnimation' frames=len(theta_list)=1000, then i=1,2,3.....,1000
        x, y = bobs_position(theta_list[i]) #finding out the position of bob in respect of theta(t)
        line.set_data([0, x], [0, y]) #also calculating the position of pendulum rod in respect of theta(t)
        bob.set_center((x, y)) #positioning the bob, such that it looks like ,it is at the end tip of rod
        return PENDULUM
    
    # Setting up the animation
    ANIMATION = FuncAnimation(fig,dynamic_fig,init_func=canvas,frames=len(theta_list),repeat=True,interval=1,blit=True,)
       # Interval=time between frames in milliseconds 
       # and  blit=True means that the animations display much more quickly. 
    plt.show()

    return ANIMATION

#The given DEs
f1 = lambda t, theta, v, g, L: (v, -(g / L) * math.sin(theta))

#Testing the function
solveDEs(DEs=f1, theta0=math.pi / 3, dTheta_dt0=0, h=0.001, t0=0, t_max=20)
