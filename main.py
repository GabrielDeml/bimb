from Agents import Agents

if __name__ == '__main__':
    print("Running BIMB")
    agents = Agents(10)
    for i in range(10000000):
        agents.test_agents()
        agents.agents_breed()
        print("Generation: " + str(i))
    print("All time top dog with fitness: " + str(agents.top_dog_fitness) + " and weights and bias" + str(agents.top_dog.weights) + " and " + str(agents.top_dog.bias))
