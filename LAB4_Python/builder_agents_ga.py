import random
import copy

# Material prices
PRICES = {
    'door': 2500,
    'outside_door': 8500,
    'window': 3450,
    'wall_module': 75000,
    'toilet_seat': 2995,
    'tab': 2350,
    'shower_cabin': 8300
}

# Needed materials for 1 house
HOUSE_REQUIREMENTS = {
    'window': 14,
    'door': 6,
    'outside_door': 1,
    'wall_module': 7,
    'toilet_seat': 2,
    'tab': 2,
    'shower_cabin': 2
}

class MaterialProviderAgent:
    def __init__(self):
        self.inventory = {}

    def replenish(self):
        self.inventory = {
            'window': 1000,
            'door': 500,
            'outside_door': 200,
            'wall_module': 1000,
            'toilet_seat': 500,
            'tab': 500,
            'shower_cabin': 500
        }

    def provide(self, material, quantity):
        available = min(self.inventory.get(material, 0), quantity)
        self.inventory[material] -= available
        return available

class BuilderAgent:
    def __init__(self, provider):
        self.provider = provider
        self.inventory = {key: 0 for key in PRICES}
        self.house_count = 0
        self.money = 0
        self.strategy = {material: random.randint(5, 25) for material in PRICES}  # Strategy for buying materials

    def acquire_material(self, material, quantity):
        self.inventory[material] += quantity

    def build_house(self):
        can_build = True
        for item, required in HOUSE_REQUIREMENTS.items():
            if self.inventory.get(item, 0) < required:
                can_build = False
                break

        while can_build:
            for item, required in HOUSE_REQUIREMENTS.items():
                self.inventory[item] -= required

            self.house_count += 1
            self.money += self.calculate_house_value()

            can_build = all(self.inventory[item] >= count for item, count in HOUSE_REQUIREMENTS.items())

    def calculate_house_value(self):
        cost = sum(HOUSE_REQUIREMENTS[item] * PRICES[item] for item in HOUSE_REQUIREMENTS)
        return int(cost * 1.10)  # 10% profit

    def clone(self):
        return copy.deepcopy(self)

# Evolution operators

def selection(population):
    sorted_agents = sorted(population, key=lambda a: (a.house_count, a.money), reverse=True)
    return [sorted_agents[i].clone() for i in range(len(population)//2)]  # Top 50%

def crossover(agent1, agent2):
    for material in PRICES:
        if random.random() < 0.5:
            # Exchange inventory
            agent1.inventory[material], agent2.inventory[material] = agent2.inventory[material], agent1.inventory[material]
        if random.random() < 0.5:
            # Exchange strategy
            agent1.strategy[material], agent2.strategy[material] = agent2.strategy[material], agent1.strategy[material]

def mutation(agent):
    material = random.choice(list(PRICES.keys()))

    # Mutate inventory
    if random.random() < 0.5:
        agent.inventory[material] = max(0, agent.inventory[material] - random.randint(1, 3))
    else:
        agent.inventory[material] += random.randint(1, 3)

    # Mutate strategy
    if random.random() < 0.5:
        change = random.randint(-3, 3)
        agent.strategy[material] = max(1, agent.strategy[material] + change)

def evaluate(population):
    sorted_agents = sorted(population, key=lambda a: (a.house_count, a.money), reverse=True)
    while len(sorted_agents) < 10:
        sorted_agents.append(sorted_agents[random.randint(0, len(sorted_agents) - 1)].clone())
    return sorted_agents

# Main function

def main():
    provider = MaterialProviderAgent()
    population = [BuilderAgent(provider) for _ in range(10)]

    for generation in range(500):
        provider.replenish()

        for agent in population:
            agent.inventory = {key: 0 for key in PRICES}  #Reset inventory

        for material in PRICES:
            amount_requested = agent.strategy[material]
            amount_received = provider.provide(material, amount_requested)
            agent.acquire_material(material, amount_received)  #Fixed acquisition bug

        agent.build_house()

        population = selection(population)

        for i in range(0, len(population), 2):
            if i + 1 < len(population):
                crossover(population[i], population[i + 1])

        for agent in population:
            mutation(agent)

        population = evaluate(population)

        print(f"\nGeneration {generation + 1}")
        for i, agent in enumerate(population):
            print(f" Agent {i + 1}: Houses Built = {agent.house_count}, Money Earned = {agent.money}")

        if population[0].house_count > 10:
            break

    print("\nFinal Results:")
    print(f"Best agent built {population[0].house_count} houses and earned {population[0].money} money.")
    print("Strategy of best agent:")
    for material, quantity in population[0].strategy.items():
        print(f"  {material}: {quantity}")

if __name__ == "__main__":
    main()
