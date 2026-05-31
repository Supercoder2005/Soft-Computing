'''
The question written in the image is:

Solve the Air Conditioner Controller Problem using Fuzzy Inference System. Frame the rules and compare the results using Mamdani, Sugeno and Tsukamoto methods.**
Rules of Temperature, Humidity and Compressor Speed:
> 1. Very Low + Dry → Off
> 2. Very Low + Comfortable → Off
> 3. Very Low + Humid → Off
> 4. Very Low + Sticky → Low
> 5. Low + Dry → Off
> 6. Low + Comfortable → Off
> 7. Low + Humid → Low
> 8. Low + Sticky → Medium
> 9. High + Dry → Low
> 10. High + Comfortable → Medium
> 11. High + Humid → Fast
> 12. High + Sticky → Fast
> 13. Very High + Dry → Medium
> 14. Very High + Comfortable → Fast
> 15. Very High + Humid → Fast
> 16. Very High + Sticky → Fast

Input Variables:
Temperature: 0-40
Humidity: 0-100 

Output Variable:
Compressor Speed: Off, Low, Medium, Fast

'''

def triangular_mf(x,a,b,c):
    if x<=a:
        return 0.0
    elif x>a and x<=b:
        return (x-a)/(b-a)
    elif x>b and x<=c:
        return (b-x)/(b-c)
    else:
        return 0.0
    
rules = [
    ("Very Low","Dry","Off"),
    ("Very Low","Comfortable","Off"),
    ("Very Low","Humid","Off"),
    ("Very Low","Sticky","Low"),
    ("Low","Dry","Off"),
    ("Low","Comfortable","Off"),
    ("Low","Humid","Low"),
    ("Low","Sticky","Medium"),
    ("High","Dry","Low"),
    ("High","Comfortable","Medium"),
    ("High","Humid","Fast"),
    ("High","Sticky","Fast"),
    ("Very High","Dry","Medium"),
    ("Very High","Comfortable","Fast"),
    ("Very High","Humid","Fast"),
    ("Very High","Sticky","Fast")
]

def fuzzify_temp(temp):
    return{
        "Very Low" : triangular_mf(temp,0,0,15),
        "Low" : triangular_mf(temp,10,20,25),
        "High" : triangular_mf(temp,20,30,35),
        "Very High" : triangular_mf(temp,30,40,40)
    }

def fuzzify_humid(humid):
    return{
        "Dry" : triangular_mf(humid,0,0,25),
        "Comfortable" : triangular_mf(humid,20,35,50),
        "Humid" : triangular_mf(humid,45,60,75),
        "Sticky" : triangular_mf(humid,70,100,100)
    }

def mamdani(temp,humid):
    T = fuzzify_temp(temp)
    H = fuzzify_humid(humid)
    speed_values = {
        "Off":0,
        "Low":30,
        "Medium":60,
        "Fast":100
    }
    numerator = 0
    denominator = 0
    for t,h,s in rules:
        res_mu = min(T[t],H[h])
        numerator += res_mu * speed_values[s]
        denominator += res_mu 
    if denominator == 0:
        return 0
    return numerator/denominator 

# Convert Crisp Output to Label
def get_speed_label(speed):

    memberships = {
        "Off": triangular_mf(speed, 0, 0, 30),
        "Low": triangular_mf(speed, 20, 35, 50),
        "Medium": triangular_mf(speed, 45, 60, 75),
        "Fast": triangular_mf(speed, 70, 100, 100)
    }

    return max(memberships, key=memberships.get)
               
               
temp = float(input("Temperature (0-40): "))
humid = float(input("Humidity (0-100): "))
speed = mamdani(temp,humid)
print("Fan speed (Mamdani Output)  :", speed)
print("Fan speed label (Mamdani)   :", get_speed_label(speed))