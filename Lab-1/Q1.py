#Q1-Assignment-1-Solution
from matplotlib import pyplot as plt
import math
n=int(input("Enter the value of n=  "))
first_funcn=[]
second_funcn=[]
y1=0
x=[]
for i in range(1,n+1):
    y1=y1+ math.log(i)  #finding first function values corresponding to i = 1,2,..,n
    y2=i*math.log(i)-i+(math.log(2*math.pi*i))/2  # #finding second function values corresponding to i = 1,2,..,n
    first_funcn.append(y1)
    second_funcn.append(y2)
    x.append(i)
#print('X-axis values',x)
#plotting the graph of both function
plt.plot(x,first_funcn, label = 'log(n!)')
plt.plot(x,second_funcn, label = 'log(2.pi.n)/2 + n.log(n) -n')
plt.legend()
plt.show()