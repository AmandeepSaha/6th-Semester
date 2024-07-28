import numpy as np
import matplotlib.pyplot as plt
# from scipy.constants import k, h ,c
k = 1.380649e-23
h = 6.62607015e-34
c = 299792458.0

# nu = np.linspace(0,100,10000)
L=np.linspace(1e-7,2e-6,5000)
T = np.arange(1000,10001,1000)
# x = (h*c)/((L*k*T))
def Plank(T):
    return ((8*np.pi*h*c)/(L**5))*(1/(np.exp((h*c)/(L*k*T))-1))

def RJ(T):
    return ((8*np.pi*k*T)/(L**4))


plt.subplot(1,2,1)
plt.title("Plank's Distribution")
plt.xlabel(r"$\lambda$")
plt.ylabel(r"$u(\lambda)$")

for i in T:
    plt.plot(L,Plank(i),label=f"T={i}k")
plt.legend(loc="upper right")

plt.subplot(1,2,2)
plt.title("Raleigh-Jeans")
plt.xlabel(r"$\lambda$")
plt.ylabel(r"$u(\lambda)$")
plt.xlim(0,2e-6)
plt.ylim(0,1.75e7)
for i in T:
    plt.plot(L,RJ(i),label=f"T={i}k")
plt.legend(loc="upper right")

plt.tight_layout()
plt.show()