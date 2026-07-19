import random 
weights = [2,3,4,5,9]
values = [3,4,5,8,10]
# Max capacity of the knapsack
capacity = 10
# no of items in the knapsack
n = len(weights)

# parameters of GA
POP_SIZE = 6
GENERATIONS = 20
MUTATION_RATE = 0.2

#--------------Fitness Function--------------
def fitness(chromosome):
    total_weight = 0
    total_value = 0
    for i in range(n):
        if chromosome[i] == 1:
            total_weight += weights[i]
            total_value += values[i]
    if total_weight > capacity:
        return 0
    return total_value 

#----------------Population------------------
population = []
for i in range(POP_SIZE):
    chromosome = []
    for j in range(n):
        chromosome.append(random.randint(0,1))
    population.append(chromosome)

#---------------Genetic Algorithm------------
for epoch in range(GENERATIONS):
    # sort in descending order as higher fitness value is better
    population.sort(key = fitness,reverse = True)
    #-------------Selection---------------
    parent1 = population[0]
    parent2 = population[1]
    #------------Crossover(Binary)--------------
    point = random.randint(1,n-1)
    child = parent1[:point]+parent2[point:]
    #-----------------Mutation------------------
    if random.random() < MUTATION_RATE:
        # select random gene from a chromosome
        i = random.randint(0,n-1)
        # flip the bit
        if child[i] == 1:
            child[i] = 0
        else:
            child[i] = 1
    #--------------Replacement----------------
    population[-1] = child 
    #-------------Generation Best---------------
    population.sort(key=fitness,reverse=True)
    best = population[0]
    print("Generation : ",epoch+1,"Best Chromosome : ",best,"Best Value : ",fitness(best))\
    
best = population[0]
total_weight = 0
total_value = 0
for i in range(n):
    if best[i] == 1:
        total_weight += weights[i]
        total_value += values[i]
print("Final Best Chromosome : ",best)
print("Final total weight : ",total_weight)
print("Final total value : ",total_value)




