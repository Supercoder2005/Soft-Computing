''' 
Rule 1 : if bp is high and temp is high then health is poor
Rule 2 : if bp is normal and temp is normal then health is good
Rule 3 : if bp is low and temp is normal then health is normal
Take the values of bp and temp as user input and determine the health of the person 
'''
def trapezoidal_mf(x,a,b,c,d):
    if x<=a:
        return 0.0
    elif x>a and x<=b :
        return (x-a)/(b-a)
    elif x>b and x<=c:
        return 1.0
    elif x>c and x<=d:
        return (d-x)/(d-c)
    else:
        return 0.0
    
# Blood Pressure (trapexoidal)
# Low bp --> 1.0 upto 80, 0.0 at 100
# Normal bp --> rises from (60-80), flat (80-120), falls (120-140)
# High bp --> rises (120-140), 1.0 after 140

def bp_low(x):
    if x<=80:
        return 1.0
    else:
        return trapezoidal_mf(x,80,80,80,100)

def bp_normal(x):
    return trapezoidal_mf(x,60,80,120,140)

def bp_high(x):
    if x>=140:
        return 1.0
    else:
        return trapezoidal_mf(x,120,140,140,140)

# Temperature (TRapezoidal)
# Normal --> rises(35-36), flat(36-37), falls(37.5-39)
# High --> rises(37.5-39, full 1.0 after 39)

def temp_normal(x):
    return trapezoidal_mf(x,35,36,37.5,39)

def temp_high(x):
    if x>=39:
        return 1.0
    else:
        return trapezoidal_mf(x,37.5,39,39,39)
    
bp = float(input("Enter the Blood Pressure : "))
temp = float(input("Enter the Temperature : "))

mu_bp_high = bp_high(bp)
mu_bp_normal = bp_normal(bp)
mu_bp_low = bp_low(bp)
mu_temp_high = temp_high(temp)
mu_temp_normal = temp_normal(temp)

print(f"BP --> Low : {mu_bp_low}, Normal : {mu_bp_normal}, High : {mu_bp_high}")
print(f"TEMP --> Normal : {mu_temp_normal}, High : {mu_temp_high}")

# Applying Rules using AND operation on fuzzy sets temp and bp
rule1 = min(mu_bp_high,mu_temp_high)
rule2 = min(mu_bp_normal,mu_temp_normal)
rule3 = min(mu_bp_low,mu_temp_normal)

health = {
    "Poor":rule1,
    "Good":rule2,
    "Normal":rule3
}

result = max(health,key=health.get)
print(f"Health of the person is : {result}, with membership value = {health[result]}")