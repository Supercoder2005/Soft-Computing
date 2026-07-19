def trapezoidal(x,a,b,c,d):
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

# Blood Pressure (trapezoidal)
# low bp ---> 1.0 upto 80 & 0.0 at 100
# normal bp ---> rises from (60-80), flat(80-120), falls(120-140)
# high bp ---> rises (120-140), 1.0 after 140

def low_bp(x):
    if x<=80:
        return 1.0
    else:
        return trapezoidal(x,80,80,80,100)
    
def normal_bp(x):
    return trapezoidal(x,60,80,120,140)

def high_bp(x):
    if x>=140:
        return 1.0
    else:
        return trapezoidal(x,120,140,140,140)
    
# Temperature (Trapezoidal)
# normal temp ---> rises(35-36),flats(36-37.5),falls(37.5-39)
# high temp ---> rises(37.5-39), 1.00 after 39 
def normal_temp(x):
    return trapezoidal(x,35,36,37.5,39)

def high_temp(x):
    if x>=39:
        return 1.0
    else:
        return trapezoidal(x,37.5,39,39,39)

bp = float(input("Enter the Blood Pressure : "))
temp = float(input("Enter the Temperature : "))

mu_low_bp = low_bp(bp)
mu_normal_bp = normal_bp(bp)
mu_high_bp = high_bp(bp)
mu_normal_temp = normal_temp(temp)
mu_high_temp = high_temp(temp)

print(f"Bp ---> Low : {mu_low_bp}, Normal : {mu_normal_bp}, High : {mu_high_bp}")
print(f"Temp ---> Normal : {mu_normal_temp}, High : {mu_high_temp}")

# Applying rules using AND operation
rule1 = min(mu_high_bp,mu_high_temp)
rule2 = min(mu_normal_bp,mu_normal_temp)
rule3 = min(mu_low_bp,mu_normal_temp)

health = {
    "Poor":rule1,
    "Good":rule2,
    "Normal":rule3
}

result = max(health,key=health.get)
print(f"Health of the person is : {result}, with membership value = {health[result]}")