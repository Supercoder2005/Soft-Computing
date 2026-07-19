import random

# Distance matrix
d = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# -------------------------------
# Fitness Function
# -------------------------------
def dist(route):
    total_dist = 0

    for i in range(len(route) - 1):
        total_dist += d[route[i]][route[i + 1]]

    # Return to starting city
    total_dist += d[route[-1]][route[0]]

    return total_dist


# -------------------------------
# Parameters
# -------------------------------
POP_SIZE = 6
GENERATIONS = 100
MUTATION_RATE = 0.1

cities = [0, 1, 2, 3]


# -------------------------------
# Initial Population
# -------------------------------
population = []

for i in range(POP_SIZE):
    route = cities.copy()
    random.shuffle(route)
    population.append(route)


# -------------------------------
# Genetic Algorithm
# -------------------------------
for epoch in range(GENERATIONS):

    # -------- Selection --------
    # Sort population according to distance
    population.sort(key=dist)

    # Select two best parents
    parent1 = population[0]
    parent2 = population[1]


    # -------- Crossover --------
    # Order Crossover (OX)
    start, end = sorted(random.sample(range(4), 2))

    child = [None] * 4

    # Copy part of Parent 1
    child[start:end] = parent1[start:end]

    # Fill remaining cities from Parent 2
    remaining = []

    for city in parent2:
        if city not in child:
            remaining.append(city)

    j = 0

    for i in range(4):
        if child[i] is None:
            child[i] = remaining[j]
            j += 1


    # -------- Mutation --------
    if random.random() < MUTATION_RATE:

        i, j = random.sample(range(4), 2)

        # Swap two cities
        child[i], child[j] = child[j], child[i]


    # -------- Replacement --------
    # Replace worst solution with new child
    population[-1] = child

    # -------- Generation Best --------
    population.sort(key=dist)

    best = population[0]

    print(
        "Generation:", epoch + 1,
        "| Best Route:", best,
        "| Distance:", dist(best)
    )


# -------------------------------
# Output
# -------------------------------
print("Final Best Route:", population[0])
print("Final Minimum Distance:", dist(population[0]))