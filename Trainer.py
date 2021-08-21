import gym
import time


class Trainer:
	def __init__(self, gui : bool = False):
		self.gui = gui
		print("Trainer initialized")
	
	def test(self, agent):
		reward_out = 0
		env = gym.make('CartPole-v0')
		if self.gui:
			env.render()
			time.sleep(1)
		state = (0, 0, 0, 0)
		env.reset()
		for i in range(10000):
			state, reward, done, info = env.step(agent.get_action(state))
			reward_out += reward
			if self.gui:
				env.render()
			# print("State: " + str(state) + " Reward: " + str(reward) +
			# 	" Done: " + str(done) + " Info: " + str(info))
			if done:
				break
		env.close()
		return reward_out