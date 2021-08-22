from Agent import Agent
from Trainer import Trainer

if __name__ == "__main__":
    agent = Agent()
    trainer = Trainer(True)
    agent.weights = [0, 0, 0, 0]
    agent.bias = [0, 0, 0, 0]
    print(trainer.test(agent))
