import random

# -------------------------------
# Problem Data
# -------------------------------

# Weight of each item
weights = [2, 3, 4, 5, 9]

# Value of each item
values = [3, 4, 5, 8, 10]

# Maximum capacity of knapsack
capacity = 10


# -------------------------------
# Parameters
# -------------------------------

POP_SIZE = 6
GENERATIONS = 20
MUTATION_RATE = 0.1

# Number of items
n = len(weights)


# -------------------------------
# Fitness Function
# -------------------------------

def fitness(chromosome):

    total_weight = 0
    total_value = 0

    for i in range(n):

        # If chromosome contains 1,
        # select the item
        if chromosome[i] == 1:

            total_weight += weights[i]
            total_value += values[i]

    # If weight exceeds capacity,
    # fitness is 0
    if total_weight > capacity:
        return 0

    return total_value


# -------------------------------
# Initial Population
# -------------------------------

population = []

for i in range(POP_SIZE):

    chromosome = []

    for j in range(n):

        # Randomly generate 0 or 1
        chromosome.append(random.randint(0, 1))

    population.append(chromosome)


# -------------------------------
# Genetic Algorithm
# -------------------------------

for epoch in range(GENERATIONS):

    # -------- Selection --------

    # Sort population according to fitness
    # Higher fitness is better
    population.sort(key=fitness, reverse=True)

    # Select two best parents
    parent1 = population[0]
    parent2 = population[1]


    # -------- Crossover --------

    # Select one random crossover point
    point = random.randint(1, n - 1)

    # Create child
    child = parent1[:point] + parent2[point:]


    # -------- Mutation --------

    if random.random() < MUTATION_RATE:

        # Select random gene
        i = random.randint(0, n - 1)

        # Flip the bit
        if child[i] == 0:
            child[i] = 1
        else:
            child[i] = 0


    # -------- Replacement --------

    # Replace worst solution with new child
    population[-1] = child


    # -------- Generation Best --------

    # Sort again after adding child
    population.sort(key=fitness, reverse=True)

    best = population[0]

    print(
        "Generation:", epoch + 1,
        "| Best Chromosome:", best,
        "| Value:", fitness(best)
    )


# -------------------------------
# Final Output
# -------------------------------

best = population[0]

total_weight = 0
total_value = 0

for i in range(n):

    if best[i] == 1:
        total_weight += weights[i]
        total_value += values[i]


print("\nFinal Best Chromosome:", best)
print("Final Total Weight:", total_weight)
print("Final Total Value:", total_value)