def bell(x,a,b,c):
    return 1/(1+abs((x-c)/a)**(2*b))

x = int(input("Enter your age : "))

young = bell(x,20,2,0)
old = bell(x,30,3,100)

more_or_less_young = young**0.5
young_but_not_too_young = min(young,(1-young**2))
not_young_and_not_old = min((1-young),(1-old))
extremely_old = old**3

print("Membership value for more or less young = ",more_or_less_young)
print("Membership value for young but not too young = ",young_but_not_too_young)
print("Membership value for not young and not old = ",not_young_and_not_old)
print("Membership value for extremely old = ",extremely_old)

