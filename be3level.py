import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import k

def f(E):
    Z = np.exp(0) + np.exp(-2*E) + 2*np.exp(-E)
    E_av = (0*np.exp(0) + (-2*E)*np.exp(-2*E) + (-E)*np.exp(-E))/Z
    C_v_ = C_v(T())
    return np.array([Z,E_av,C_v_])

def C_v(T):
    # E = 1
    Z = np.exp(0) + np.exp(-2/(T)) + 2*np.exp(-1/(T))
    E_av = (1*0 + 2 * np.exp(-2/(T)) + 1 * np.exp(-1/(T)))/Z
    E_sq_av = ((2**2)*np.exp(-2/(T))+1*np.exp(-1/(T)))/Z
    return (E_sq_av - E_av)/(T**2)
    
def L(x):
    l = np.array(["Z","{E_{average}}","C_v"])
    return l[x]

def T():
    return np.linspace(0.01,4,1000)

def E():
    return np.arange(0,10,0.01)

def graphing():
    fig , ax = plt.subplots(1,3,figsize=(9,10))
    for i, e in enumerate(f(E())):
        ax[i].set_title(r"E vs ${}$".format(L(i)))
        ax[i].set_xlabel(r"$E\longrightarrow$")
        ax[i].set_ylabel(r"${}\longrightarrow$".format(L(i)))
        ax[i].plot(E(),e)
    plt.tight_layout()
    plt.show()
    
# print(C_v(T()))
graphing()