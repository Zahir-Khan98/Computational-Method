from matplotlib import pyplot as plt
import numpy as np

M = 200 # setting the max number of interval

trapezoidal_integration = [] #we'll append the approximated integration value for each value of "no. of intervals" (M)

I = 0 #I is for calculating the sum of {f(X_i)+f(X_i-1)} over i= 1,.... ,M+1
x = 1
for i in range(2, M + 1): #loop is starting from 2, as there should be minimum 2 intervals

    x = 1 #as the main interval is [1,3]

    h = 2 / i #as for [a,b]. space value h = (b-a)/(no. of intervals)

    while x+h <= 3:#as our main interval is [1,3]
        # calculating the sum in the trapezoidal value
        I = I + ((2*x*np.e**(x**2))+(2*(x+h)*np.e**((x+h)**2)))/2
        x = x + h
    trapezoidal_integration.append(h *I)
    I = 0

x = np.linspace(2, M, M-1) # setting x_axis values
# plotting the values
fig, ax = plt.subplots()
ax.plot(x, trapezoidal_integration,label=" Approximated value of area by Trapezoidal rule")
plt.grid(True, which="both")
plt.axhline(y=np.e ** 9 - np.e,color="r",label="Exact value of Area")
ax.set_xlabel("Number of intervals")
ax.set_ylabel("Value of Area")
ax.set_title("Area under the curve $2xe^{x^2}$")
ax.legend()
plt.show()

