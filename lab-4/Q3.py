from matplotlib import pyplot as plt
import numpy as np
import math

h = np.linspace(0.001,0.5, 25)
x = np.linspace(0, 1, 25)
max_abs_error_list_of_FD = [] #for each value value of h, we'll find max absolute error of FD
max_Th_ERRs_FD_list=[] #for each value value of h, we'll find max Theoretical error of FD
max_abs_error_list_of_CD = [] #for each value value of h, we'll find max absolute error of CD
max_Th_ERRs_CD_list =[] #for each value value of h, we'll find max Theoretical error of CD
for i in h:
    # for each i calculating all the absolute max error values for forward difference 
    abs_Errors_of_FD = [abs(np.cos(j ** 2) * 2 * j - (np.sin((j + i) ** 2) - np.sin(j ** 2)) / i) for j in x]
    # for each i calculating all the absolute max error values for centered  difference
    abs_Errors_of_CD = [abs(np.cos(j ** 2) * 2 * j- (np.sin(math.pow(j + i, 2)) - np.sin(math.pow(j - i, 2))) / (2 * i) )  for j in x]
    # for each i calculating all the theoretical error values for forward,centered  difference
    for j in x:
        jai_values = np.linspace(j,j+i,50)
        Th_ERRs_FD=[abs(i*(np.cos(jai**2)- 2*jai**2*np.sin(jai**2))) for jai in jai_values]
        TH_ERRs_CD=[(i**2)/6*abs(-12*jai*np.sin(jai**2)-8*(jai**3)*np.cos(jai**2)) for jai in jai_values]
    
    # appending the max errors
    max_abs_error_list_of_FD.append(max(abs_Errors_of_FD))
    max_abs_error_list_of_CD.append(max(abs_Errors_of_CD))
    max_Th_ERRs_FD_list.append(max(Th_ERRs_FD))
    max_Th_ERRs_CD_list.append(max(TH_ERRs_CD))
    #clearing the lists for next iteration
    abs_Errors_of_FD.clear()
    abs_Errors_of_CD.clear()
    Th_ERRs_FD.clear()
    TH_ERRs_CD.clear()
# plotting the values for visulization

fig, ax = plt.subplots()
ax.plot(x, max_abs_error_list_of_FD,"r",label="Max Absolute Error of Forward difference")
ax.plot(x, max_Th_ERRs_FD_list,"y",label="Max Theoretical Error of Forward difference")
ax.plot(x,max_abs_error_list_of_CD,"b",label="Max Absolute Error of Centred Difference")
ax.plot(x, max_Th_ERRs_CD_list,"g",label="Max Theoretical Error of Centered difference")
plt.grid(True, which="both")
ax.set_xlabel("h-values")
ax.set_ylabel("Maximum Error value")
ax.set_title("Visulization of max absolute and theoritical error value for different values of h")
ax.legend()
plt.show()


