# Q.3 of Assignment-1
from matplotlib import pyplot as plt
import random
import math
n = int(input("Enter the number of points to generate: ")) #taking total number of generating points
def estimatePi(n):
    inside_circle = 0 #initially we are allocating 0 points inside the circle
    j = []
    for i in range(1,n+1):
        #taking random x-points and y points from (-1,1) to create (x,y) points
        x = random.uniform(-1, 1) 
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1: # checking if the point is inside the inscribed circle or not
            inside_circle += 1
        j.append(4*inside_circle/i)       
    pi_estimate = 4*inside_circle/n #applying Monte-Carlo formula for estimsating pi. 
    print("Estimate of math.pi using Monte carlo method is:", pi_estimate)
    #ploting the exact pi value and estimated pi value
    plt.plot(range(1,n+1), j , label='Monte Carlo method')
    pi=math.pi
    plt.axhline(pi , color='r', label='Value of pi')
    plt.legend()
    plt.show()
estimatePi(n)
