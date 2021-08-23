import random


class Agent:
    weights = [0, 0, 0, 0]
    bias = [0, 0, 0, 0]

    def __init__(self, r=False):
        if r:
            for i in range(len(self.weights)):
                self.weights[i] = random.uniform(-1, 1)
                self.bias[i] = random.uniform(-1, 1)

    def get_action(self, state):
        out = 0
        for i in range(len(self.weights)):
            out += (self.weights[i] * state[i]) + self.bias[i]
        return 1 if out > 0 else 0

    def mutate(self):
        pram_to_change = random.randint(
            0, len(self.weights) + len(self.bias) - 1)
        if pram_to_change < len(self.weights):
            self.weights[pram_to_change] += random.uniform(-0.01, 0.01)
        else:
            # print(str(pram_to_change - len(self.weights)))
            self.bias[pram_to_change -
                      len(self.weights)] += random.uniform(-0.01, 0.01)
