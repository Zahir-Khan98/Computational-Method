import math
from matplotlib import pyplot as plt
import numpy as np
fig,ax=plt.subplots()
x=np.linspace(0,1.0,num=10) #taking the partition of [0,1]
#fol: below calculating true value of the derivative using derivative formula
y_der=[np.cos(math.pow(i,2))*2*i for i in x]
#fol: below calculating forward difference approximation for each x in [0,1]
Forward_FD=[(np.sin(math.pow(i+0.01,2))-np.sin(math.pow(i,2)))/0.01 for i in x] # we took h=0.01
#fol: below calculating backward difference approximation for each x in [0,1]
Backward_FD=[(np.sin(math.pow(i,2))-np.sin(math.pow(i-0.01,2)))/0.01 for i in x]
#fol: below calculating Centered difference approximation for each x in [0,1]
Centered_FD=[(np.sin(math.pow(i+0.01,2))-np.sin(math.pow(i-0.01,2)))/(2*0.01) for i in x]
#fol: below calculating error approximation of Forward,Backward,Centered difference
Forward_FD_Err=[abs(y_der[i]-Forward_FD[i]) for i in range(len(x))]
Backward_FD_Err=[abs(y_der[i]-Backward_FD[i]) for i in range(len(x))]
Centered_FD_Err=[abs(y_der[i]-Centered_FD[i]) for i in range(len(x))]
# plotting of values
ax.plot(x,Forward_FD_Err,"g",label="Forward Difference")
ax.plot(x,Centered_FD_Err,"b",label="Centered difference")
ax.plot(x,Backward_FD_Err,"r",label="Backward difference")
ax.set_xlabel("x")
ax.set_ylabel("Error in Approximation")
ax.set_title("Plot of Error Approximations in Numerical Differentiation")
plt.grid(True,which="both")
ax.legend()
plt.show()