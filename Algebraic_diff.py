import numpy as np 
import matplotlib.pyplot as plt 

def triangular_mf(x,a,b,c):
    mu = []
    for value in x:
        if value<=a:
            mu.append(0)
        elif a<value<=b:
            mu.append((value-a)/(b-a))
        elif b<value<=c:
            mu.append((c-value)/(c-b))
        else:
            mu.append(0)
    return np.array(mu)
x = np.linspace(0,10,1000)
set1 = triangular_mf(x,1,3,5)
set2 = triangular_mf(x,2,4,6)
algebraic_diff = set1*(1-set2)
plt.plot(x,set1)
plt.plot(x,set2)
plt.plot(x,algebraic_diff)
plt.fill_between(x,algebraic_diff,color='magenta',alpha=0.2)
plt.title("Triangular Membership Function -- Algebraic Difference")
plt.xlabel("Universe of Discourse")
plt.ylabel("Membership Value")
plt.grid(True)
plt.show()
            



