import gym
import time


class Trainer:
    def __init__(self, gui=False):
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
        count = 0
        for i in range(250):
            state, reward, done, info = env.step(agent.get_action(state))
            reward_out += reward

            if self.gui:
                env.render()
            # print("State: " + str(state) + " Reward: " + str(reward) +
            # 	" Done: " + str(done) + " Info: " + str(info))
            if done:
                count = i
                break
        # print(str(count) + " steps taken")
        env.close()
        return count
