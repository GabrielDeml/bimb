from Agent import Agent
from Trainer import Trainer
import copy


import multiprocessing


class Agents:
    number_of_agents = 0

    def __init__(self, number_of_agents):
        self.number_of_agents = number_of_agents

        self.trainer = Trainer()

    def generate_agents(self):
        agents = []
        for i in range(self.number_of_agents):
            agents.append(Agent())
        return agents

    def agent_test(self, agent):
        return self.trainer.test(agent)

    def test_agents(self, agents):
        top_dog = agents[0]
        top_dog_fitness = 0
        # for agent in self.agents:
        pool = multiprocessing.Pool(processes=4)
        agents_scores = pool.map(self.agent_test, agents)
        for i in range(len(agents_scores)):
            if agents_scores[i] > top_dog_fitness:
                top_dog = agents[i]
                top_dog_fitness = agents_scores[i]
                # if agents_scores[i] > self.top_dog_all_time_fitness:
                #     self.top_dog_all_time_weights = self.agents[i].weights
                #     self.top_dog_all_time_bias = self.agents[i].bias
                #     self.top_dog_all_time_fitness = copy.deepcopy(agents_scores[i])
        return top_dog, top_dog_fitness

    def agents_breed(self, top_dog):
        agents = []
        for i in range(self.number_of_agents):
            tmp = copy.deepcopy(top_dog)
            tmp.mutate()
            agents.append(tmp)
        return agents
