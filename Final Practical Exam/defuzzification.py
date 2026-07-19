n = int(input("Enter the number of elements in the fuzzy set : "))
elements = []
for i in range(n):
    elements.append(float(input(f"Enter element {i+1} :")))
memberships = []
for i in range(n):
    memberships.append(float(input(f"Enter membership value for element {i+1} : ")))
print("Elements : ",elements)
print("Memberships : ",memberships)

# Centroid of Area (COA)
numerator = 0
denominator = 0
for i in range(n):
    numerator += elements[i]*memberships[i]
    denominator += memberships[i]
coa = numerator/denominator

# Bisector of Area (BOA)
total = sum(memberships)
cumulative = 0
boa = elements[0]
for i in range(n):
    cumulative += elements[i]
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

print("Centroid of Area = ",coa)
print("Bisector of Area = ",boa)
print("Mean of Maximum = ",mom)
print("Smallest of Maximum = ",som)
