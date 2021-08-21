from Agent import Agent
from Trainer import Trainer

if __name__ == "__main__":
	agent = Agent()
	trainer = Trainer(True)
	agent.weights = [-2.176919087490259, -5.069639855599322, 1.8296087309744997, 4.908970784001509]
	agent.bias = [-9.088401748890515, 2.026662267712265, 6.841514797148444, -1.5998583034045735]
	print(trainer.test(agent))