import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import k,e

# Temperature
def T(x):
    if x == 1:
        return np.array([0.00001,1000,2000,3000])
    else:
        return np.array([3000,5000,7000,10000])


# Chemical Potential of the system
def mu():
    return float(input("Chemical Potential :"))

# Distribution Functions
def MB(E,k,T):
    return 1/np.exp((E)/(k*T))

def BE(E,k,T,mu):
    return 1/(np.exp((E-mu)/(k*T))-1+1e-10)

def FD(E,k,T,mu):
    return 1/(np.exp((E-mu)/(k*T))+1)

# Execution
def Graphing():
    
    E = np.linspace(-1,1,1000)*e # Energy Range in Joules
    fig, ax = plt.subplots(1,3,figsize=(18,6))
    L = ["Maxwell Boltzmann Distribution","Bose Einstein Distribution","Fermi Dirac Distribution"]
    
    for i in range(3):
        
        ax[i].set_title(f"{L[i]}")
        ax[i].set_xlabel(r"$\epsilon\longrightarrow$")
        ax[i].set_ylabel(r"$f(\epsilon)\longrightarrow$")
        
        ax[i].grid(True)
        for j, temp in enumerate(T(i)):
            if i == 0:
                ax[i].plot(E,MB(E=E,k=k,T=temp),label=f"{temp}K")
                
                # print(MB(E=E,k=k,T=temp,mu=0))
            elif i==1:
                ax[i].plot(E,BE(E=E,k=k,T=temp,mu=0),label=f"{temp}K")
                ax[i].set_ylim(0,1)
                # print(BE(E=E,k=k,T=temp,mu=0))
            else:
                ax[i].plot(E,FD(E=E,k=k,T=temp,mu=0),label=f"{temp}K")
                # print(FD(E=E,k=k,T=temp,mu=0))
            ax[i].legend()
                
        plt.tight_layout()
    
    plt.show()
    
Graphing()