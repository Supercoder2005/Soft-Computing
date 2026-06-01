'''Given, following membership Punctions for fuzzy sets old and young where,
x is the age of the person . Calculate the value of the followirg :

mu_young (x) = bell (x, 20, 2, 0)
mu_old (x) = bell (x, 30, 3, 100)

More or less young                  Young but not too young
Not young and not old               Extremely old'''

import numpy as np
def bell(x,a,b,c):
    return 1/(1+(np.abs((x-c)/a)**(2*b)))

x = int(input("Enter your Age : "))
young = bell(x,20,2,0)
old = bell(x,30,3,100)

ans1 = young**0.5
ans2 = min(young,(1-young**2))
ans3 = min((1-young),(1-old))
ans4 = old**3
print("Membership value of Age for more or less young : ",ans1)
print("Membership value of Age for young but not too young : ",ans2)
print("Membership value of Age for not young and not old : ",ans3)
print("Membership value of Age for extremely old : ",ans4)