''' 
Rule 1 : if bp is high and temp is high then health is poor
Rule 2 : if bp is normal and temp is normal then health is good
Rule 3 : if bp is low and temp is normal then health is normal
Take the values of bp and temp as user input and determine the health of the person 
'''
bp = float(input("Enter your Blood Pressure : "))
temp = float(input("Enter your temperature : "))

def trapezoidal_mf(x,a,b,c,d):
    if x<=a:
        return 0.0
    elif x>a and x<=b:
        return (x-a)/(b-a)
    elif x>b and x<=c:
        return 1.0
    elif x>c and x<=d:
        return (d-x)/(d-c)
    else:
        return 0.0

# Fuzzification : BP
def low_bp(bp):
    if bp<=80:
        return 1.0
    else:
        return trapezoidal_mf(bp,80,80,80,100)

def normal_bp(bp):
    return trapezoidal_mf(bp,60,80,120,140)

def high_bp(bp):
    if bp>=140:
        return 1.0
    else:
        return trapezoidal_mf(bp,120,140,140,140)

# Fuzzification : Temp
def normal_temp(temp):
    return trapezoidal_mf(temp,35,36,37.5,39)

def high_temp(temp):
    if temp>=39:
        return 1.0
    else:
        return trapezoidal_mf(temp,37.5,39,39,39)
    
mu_low_bp = low_bp(bp)
mu_normal_bp = normal_bp(bp)
mu_high_bp = high_bp(bp)
mu_normal_temp = normal_temp(temp)
mu_high_temp = high_temp(temp)

print(f"BP --> Low : {mu_low_bp}, Normal : {mu_normal_bp}, High : {mu_high_bp}")
print(f"TEMP --> Normal : {mu_normal_temp}, High : {mu_high_temp}")

# Apply the Rules
rule1 = min(mu_high_bp,mu_high_temp)
rule2 = min(mu_normal_bp,mu_normal_temp)
rule3 = min(mu_low_bp,mu_normal_temp)

# output 
Health = {
    "Poor":rule1,
    "Good":rule2,
    "Normal":rule3
}
result = max(Health,key=Health.get)

print(f"Your Health is : {result}, with strength : {Health[result]}")