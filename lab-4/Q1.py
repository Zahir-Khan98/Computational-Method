import math
from matplotlib import pyplot as plt
import numpy as np
fig,ax=plt.subplots()
x=np.linspace(0,1.0,10) #taking the partition of [0,1]
#fol: below calculating true value of the derivative using derivative formula
y_der=[np.cos(math.pow(i,2))*2*i for i in x]
#fol: below calculating forward difference approximation for each x in [0,1]
Forward_FD=[(np.sin(math.pow(i+0.01,2))-np.sin(math.pow(i,2)))/0.01 for i in x] # taken h=0.01
# plotting the graph
ax.plot(x,y_der,"b",label="Actual value of the derivative")
ax.plot(x,Forward_FD,"r",label="Forward finte difference approximation")
plt.grid(True,which="both")
plt.xticks(x)
ax.set_xlabel("x")
ax.set_ylabel("f'(x)")
ax.set_title('Visulization of actual derivative and forward finite difference of $sin(x^2)$')
ax.legend()
plt.show()