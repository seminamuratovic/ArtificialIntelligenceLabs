# LAB 3 - Genetic Algorithm
# 
# Implement the most simple and classic genetic algorithm.
# Implement selection, crossover, and mutation of your choice.
# The genes will take binary values, either ‘0’ or ‘1’, representing yes/no answers.
#
# Each individual has a chromosome of 50 genes:
# Example:
#   Individual 1: [0 0 1 ... 1]
#   Individual 2: [0 1 1 ... 0]
#   ...
#   Individual 20: [1 1 1 ... 0]
#
# The objective is to maximize the sum of all genes.
# In other words, the goal is to evolve an individual whose chromosome consists entirely of 1s.
# The best possible individual looks like this:
#   [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
#    1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1]

import random

CHROMOSOME_LENGTH = 50
POPULATION_SIZE = 20
CROSSOVER_RATE = 0.6
MUTATION_RATE = 0.03
MAX_GENERATIONS = 1000

# Create an individual (random chromosome)
def create_individual():
    return [random.randint(0, 1) for _ in range(CHROMOSOME_LENGTH)]

# Fitness function (counts how many 1 are in the chromosome)
def fitness(individual):
    return sum(individual)

# Roulette wheel selection (select one individual based on fitness probability)
def roulette_wheel_selection(population, fitnesses):
    total_fitness = sum(fitnesses)
    pick = random.uniform(0, total_fitness)
    current = 0
    for individual, fit in zip(population, fitnesses):
        current += fit
        if current > pick:
            return individual

# Single-point crossover between two parents
def crossover(parent1, parent2):
    if random.random() < CROSSOVER_RATE:
        point = random.randint(1, CHROMOSOME_LENGTH - 1)
        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]
        return child1, child2
    else:
        return parent1[:], parent2[:]

# Mutation operation (flip bits with MUTATION_RATE probability)
def mutate(individual):
    return [1 - gene if random.random() < MUTATION_RATE else gene for gene in individual]

# Evolution: create a new generation from the current population
def evolve(population):
    new_population = []
    fitnesses = [fitness(ind) for ind in population]

    while len(new_population) < POPULATION_SIZE:
        parent1 = roulette_wheel_selection(population, fitnesses)
        parent2 = roulette_wheel_selection(population, fitnesses)
        child1, child2 = crossover(parent1, parent2)
        child1 = mutate(child1)
        child2 = mutate(child2)
        candidates = [parent1, parent2, child1, child2]
        candidates.sort(key=fitness, reverse=True)
        new_population.extend(candidates[:2])

    return new_population

# Main function: run the genetic algorithm
def run():
    population = [create_individual() for _ in range(POPULATION_SIZE)]
    generation = 0

    while generation < MAX_GENERATIONS:
        population = evolve(population)
        best = max(population, key=fitness)
        best_fitness = fitness(best)
        print(f"Generation {generation}: Best fitness = {best_fitness}")
        if best_fitness == CHROMOSOME_LENGTH:
            print("Perfect solution found!")
            print("Chromosome:", best)
            break
        generation += 1
    else:
        print("Perfect solution not found after maximum number of generations.")

run()
