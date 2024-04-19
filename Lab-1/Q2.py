#Q2 of Assignment-1
from matplotlib import pyplot as plt 
import random
import numpy
class Dice:  #creating 'Dice' class
    def __init__(self,numsides=6):
        self.numsides = numsides
        self.pmf=[] #array for probability mass function for each event
        #checking if number of sides is not valid
        if isinstance(self.numsides,int)== False or self.numsides <= 4:
            try:
                raise Exception("Cannot construct the dice")
            except Exception as l:
                print(type(l))
                print(l)
            #exit()    
        for i in range(self.numsides):
            self.pmf.append(1/self.numsides)
    def setProb(self, pmf):
        self.pmf=pmf
        if len(self.pmf) != self.numsides or sum(self.pmf) != 1: #checking if the probability distribution function is valid 
            try:
                raise Exception("invalid probability distribution")
            except Exception as m:
                print(type(m))
                print(m)
    def __str__(self):
            return f"Dice with {self.numsides} faces and probability distribution {{{str(self.pmf)[1:-1]}}}" 
    def roll(self,n):
        actual_outcome=[]      #creating arrays for actual and expected outcomes
        expected_outcome=[]
        for i in range(self.numsides):
            actual_outcome.append(0)
            expected_outcome.append(self.pmf[i]*n)
        for i in range(n):
            RandomNo=random.random() #generating random values from (0,1) to find actual outcomes
            CDF=0
            for j in range(self.numsides):
                CDF = CDF + self.pmf[j]
                if RandomNo <= CDF:
                    actual_outcome[j] += 1
                    break
         #ploting a bar chat which actual and expected outcomes
        x = numpy.arange(1,self.numsides+1)
        fig,ax = plt.subplots()
        ax.bar(x-0.05, expected_outcome,0.1, label = 'Expected Outcomes')
        ax.bar(x+0.05, actual_outcome,0.1, label = 'Actual Outcomes')
        ax.set_xlabel("Sides")
        ax.set_ylabel("Occurance")
        ax.set_xticks(x)
        plt.legend()
        plt.show()            
d=Dice(4)
d.setProb((0.1,0.2,0.3,0.4)) #giving a probability distribution for 4 face dice
print(d) # to print the details about dice
d.roll(100)  #considering 100 time rolling of dice