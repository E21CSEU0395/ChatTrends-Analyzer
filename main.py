import random

# Define the fitness function to be optimized
def fitness_function(x):
    return x ** 2

# Genetic Algorithm parameters
population_size = 50
mutation_rate = 0.1
num_generations = 100

# Generate an initial population
def initialize_population(size):
    return [random.uniform(-10, 10) for _ in range(size)]

# Select parents based on fitness
def select_parents(population):
    return sorted(population, key=fitness_function, reverse=True)[:2]

# Perform crossover to create offspring
def crossover(parent1, parent2):
    midpoint = random.randint(1, len(parent1) - 1)
    child1 = parent1[:midpoint] + parent2[midpoint:]
    child2 = parent2[:midpoint] + parent1[midpoint:]
    return child1, child2

# Perform mutation
def mutate(child):
    for i in range(len(child)):
        if random.random() < mutation_rate:
            child[i] = random.uniform(-10, 10)
    return child

# Main genetic algorithm loop
population = initialize_population(population_size)
for generation in range(num_generations):
    new_population = []

    for _ in range(population_size // 2):
        parent1, parent2 = select_parents(population)
        child1, child2 = crossover(parent1, parent2)
        child1 = mutate(child1)
        child2 = mutate(child2)
        new_population.extend([child1, child2])

    population = new_population

# Find the best solution
best_solution = max(population, key=fitness_function)
best_fitness = fitness_function(best_solution)

print("Best solution:", best_solution)
print("Best fitness:", best_fitness)
