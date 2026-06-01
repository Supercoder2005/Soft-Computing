n = int(input("Enter the number of elements in the fuzzy set :"))
elements = []
for i in range(n):
    e = int(input(f"Enter element {i+1} : "))
    elements.append(e)
print(elements)

memberships = []
for i in range(n):
    m = float(input(f"Enter membership value of element {i} : "))
    memberships.append(m)
print(memberships)

# Centroid of Mean (COM)
numerator = 0
denominator = 0
for i in range(n):
    numerator += elements[i]*memberships[i]
    denominator += memberships[i]
COM = numerator/denominator

# Bisector of Area (BOA)
totalArea = 0
for i in range(n):
    totalArea += memberships[i]
cumulative = 0
BOA = elements[0]
for i in range(n):
    cumulative += memberships[i]
    if cumulative > (totalArea/2):
        BOA = elements[i]
        break 

# Mean of Maximum (MOM)
max_membership = max(memberships)
max_elements = []
for i in range(n):
    if memberships[i] == max_membership:
        max_elements.append(elements[i])
sum = 0
for i in range(len(max_elements)):
    sum += max_elements[i]
MOM = sum/len(max_elements)

# Smallest of Maximum (SOM)
SOM = min(max_elements)

print("COM = ",COM)
print("BOA = ",BOA)
print("MOM = ",MOM)
print("SOM = ",SOM)
        
