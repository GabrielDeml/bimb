from Agent import Agent
from Trainer import Trainer

if __name__ == "__main__":
	agent = Agent()
	trainer = Trainer(True)
	agent.weights = [8.29397710683425, -20.549118275076218, -13.892203433711716, 3.6798163099757275]
	agent.bias = [-2.5521269753884805, 3.9482095212576622, 7.967595489682139, -6.362736522964777]
	trainer.test(agent)