from Agent import Agent
from Trainer import Trainer
import copy


class Agents:
    number_of_agents = 0
    agents = []
    top_dog_all_time = 0
    top_dog_all_time_fitness = 0

    def __init__(self, number_of_agents):
        self.number_of_agents = number_of_agents
        for i in range(number_of_agents):
            # print("agent: " + str(i))
            self.agents.append(Agent(True))
        self.trainer = Trainer()

    def test_agents(self):
        self.top_dog = self.agents[0]
        self.top_dog_fitness = 0
        for agent in self.agents:
            # print(agent)
            score = self.trainer.test(agent)
            if score > self.top_dog_fitness:
                self.top_dog = agent
                self.top_dog_fitness = score
                print("New top dog with fitness: " + str(self.top_dog_fitness) + " and weights and bias" + str(self.top_dog.weights) + " and " + str(self.top_dog.bias))
                if score > self.top_dog_all_time_fitness: 
                    self.top_dog_all_time = agent
                    self.top_dog_all_time_fitness = score


    def agents_breed(self):
        for i in range(self.number_of_agents):
            tmp = copy.deepcopy(self.top_dog)
            tmp.mutate()
            self.agents[i] = tmp
