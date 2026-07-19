import random 
# Distance matrix
d = [
    [0,10,15,20],
    [10,0,35,25],
    [15,35,0,30],
    [20,25,30,0]
]
# Fitness Function
def dist(route):
    total_dist = 0
    for i in range(len(route)-1):
        total_dist += d[route[i]][route[i+1]]
    total_dist += d[route[-1]][route[0]]
    return total_dist 
# Parameters of GA
POP_SIZE = 6
GENERATIONS = 100
MUTATION_RATE = 0.2

cities = [0,1,2,3]

# initial population
population = []
for i in range(POP_SIZE):
    route = cities.copy()
    random.shuffle(route)
    population.append(route)

# Genetic Algorithm
for epoch in range(GENERATIONS):

    # ----------Selection----------
    # sort population according to their distance
    population.sort(key=dist)
    # select two best parents
    parent1 = population[0]
    parent2 = population[1]

    # -------------Crossover (Order Crossover)----------
    start,end = sorted(random.sample(range(4),2))
    child = [None]*4

    # copy part of parent1 to the child ranging from start to end-1
    child[start:end] = parent1[start:end]

    # fill the remaining cities from parent2
    remaining = []
    for city in parent2:
        if city not in child:
            remaining.append(city)

    j = 0
    for i in range(4):
        if child[i] is None:
            child[i] = remaining[j]
            j += 1
    
    # ------------------Mutation--------------------
    if random.random() < MUTATION_RATE: 
        #random.random() will generate random numbers btwn 0 and 1
        i,j = random.sample(range(4),2)
        #swap two cities
        child[i],child[j] = child[j],child[i]
    
    # Replacement
    # Replace worst solution with the new child
    population[-1] = child 

    # Generation Best 
    population.sort(key=dist)
    best = population[0]
    print("Generation : ",epoch+1,"Best route : ",best,"Distance : ",dist(best))

print("Final best route : ",population[0])
print("Final minimum distance : ",dist(population[0]))



