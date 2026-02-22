import numpy as np 
import matplotlib.pyplot as plt 
def trapezoidal_mf(x,a,b,c,d):
    mu = []
    for value in x:
        if value<=a:
            mu.append(0)
        elif a<value<=b:
            mu.append((value-a)/(b-a))
        elif b<value<=c:
            mu.append(1)
        elif c<value<=d:
            mu.append((d-value)/(d-c))
        else:
            mu.append(0)
    return np.array(mu)
x = np.linspace(0,10,1000)
y = trapezoidal_mf(x,2,4,6,8)
plt.plot(x,y)
plt.title("Trapezoidal Membership Function")
plt.xlabel("Universe of Discourse")
plt.ylabel("Membership Value")
plt.grid(True)
plt.show()
        

