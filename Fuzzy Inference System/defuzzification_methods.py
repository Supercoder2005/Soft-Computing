n = int(input("Enter the number of elements in the fuzzy sets:"))
elements = []
for i in range(n):
    elements.append(float(input(f"Enter element {i+1} : ")))

memberships = []
for i in range(n):
    memberships.append(float(input(f"Enter membership value of {elements[i]} : ")))

print("Elements : ",elements)
print("Memberships : ",memberships)

# Centroid of Area (COA)
numerator = 0
denominator = 0
for i in range(n):
    numerator = numerator + elements[i]*memberships[i]
    denominator = denominator + memberships[i]
coa = numerator/denominator 

# Bisector of Area (BOA)
total = sum(memberships)
cumulative = 0
boa = elements[0]
for i in range(n):
    cumulative += memberships[i]
    if cumulative >= total/2:
        boa = elements[i]
        break 

# Mean of Maximum (MOM)
max_mu = max(memberships)
max_elements = []
for i in range(n):
    if memberships[i] == max_mu:
        max_elements.append(elements[i])
mom_sum = 0
for i in range(len(max_elements)):
    mom_sum += max_elements[i]
mom = mom_sum/len(max_elements)

# Smallest of Maximum (SOM)
som = min(max_elements)

print(f"Centroid of Area = {coa}")
print(f"Bisector of Area = {boa}")
print(f"Mean of Maximum = {mom}")
print(f"Smallest of Maximum = {som}")