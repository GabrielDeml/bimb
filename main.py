from Agents import Agents
import copy

top_dog_all_time_fitness = 0
top_dog_all_time_weights = []   
top_dog_all_time_bias = []

if __name__ == '__main__':
    print("Running BIMB")
    agents = Agents(1000)
    for i in range(10000):
        list_of_agents = agents.generate_agents()
        top_dog, top_dog_fitness = agents.test_agents(list_of_agents)
        print("Generation: " + str(i))
        print("Top dog " + str(top_dog) + " with fitness " + str(top_dog_fitness) + " weights " + str(top_dog.weights) + " bias " + str(top_dog.bias))
        if top_dog_fitness > top_dog_all_time_fitness:
            top_dog_all_time_fitness = copy.deepcopy(top_dog_fitness)
            top_dog_all_time_weights = copy.deepcopy(top_dog.weights)
            top_dog_all_time_bias = copy.deepcopy(top_dog.bias)
        print("All time top dog with fitness: " + str(top_dog_all_time_fitness) + " and weights" + str(top_dog_all_time_weights) + " and bias " + str(top_dog_all_time_bias))
        list_of_agents = agents.agents_breed(top_dog)