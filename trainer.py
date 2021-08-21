import gym
from Agent import Agent
import time

agent = Agent()
env = gym.make('CartPole-v0')
env.render()
time.sleep(1)
state = (0, 0, 0, 0)
print(env.reset())
for i in range(1000):
    state, reward, done, info = env.step(agent.get_action(state))
    env.render()
    print("State: " + str(state) + " Reward: " + str(reward) +
          " Done: " + str(done) + " Info: " + str(info))
    if done:
        env.reset()
        state = (0, 0, 0, 0)
env.close()