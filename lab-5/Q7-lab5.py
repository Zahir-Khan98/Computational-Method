import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate


# Fourier approximation of nth degree for the  function e^x
def Best_Fit_FourierApproximation(degree):
    a_k__values = []
    b_k__values = []

    for i in range(degree + 1):
        fx_Coskx = lambda x: np.exp(x) * np.cos(i * x)  # calculation for ak, here f(x)=e^x
        fx_Sinkx = lambda x: np.exp(x) * np.sin(i * x)  # calculation of bk
        a_k__values.append((1 / np.pi) * integrate.quad(fx_Coskx, -np.pi, np.pi)[0])  # storing ak values
        b_k__values.append((1 / np.pi) * integrate.quad(fx_Sinkx, -np.pi, np.pi)[0])  # stroring bk values
    # printing the co-effecients ak and bk
    print("The co-effecients of S_n(X) are as below:\n")
    print("co-effecients of cosines are ", a_k__values[1:],"\n") #a_k__values[1:] will give a_1,..,a_n. as a_0 is not a coefficient
    print("co-effecients of sines are ", b_k__values[1:])  #b_k__values[1:] will give b_1,..,b_n. as b_0 is not a coefficient
    X = np.linspace(-np.pi, np.pi, num=100)
    sn = a_k__values[0] / 2 #initiating the fourier series with a_0/2
    Sn_at_X_val = []
    # calculation of S_n(x) for all x
    for x in X:
        for k in range(1, degree + 1):
            sn = sn + a_k__values[k] * np.cos(k * x) + b_k__values[k] * np.sin(k * x)
        Sn_at_X_val.append(sn)
        sn = a_k__values[0] / 2
    #plotting    
    fig, ax = plt.subplots()
    y = [np.exp(i) for i in X]
    ax.plot(X, y,"b",linewidth= 2,  label="$e^x$")
    ax.plot(X, Sn_at_X_val,"r", label="Best fit Fourier approximation of $e^x$")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("plotting of best fit Fourier approximation of $e^x$ and actual plot of $e^x$")
    plt.grid(True, which="both")
    ax.legend()
    plt.show()
Best_Fit_FourierApproximation(8)
