from Agents import Agents

if __name__ == '__main__':
    print("Running BIMB")
    agents = Agents(100)
    for i in range(10000):
        agents.test_agents()
        agents.agents_breed()
