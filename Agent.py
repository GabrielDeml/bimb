class Agent:
    weights = [0, 0, 0.7, 0]
    bias = [0, 0, 0, 0]

    def __init__(self):
        print("Agent created")

    def get_action(self, state):
        out = 0
        for i in range(len(self.weights)):
            out += (self.weights[i] * state[i]) + self.bias[i]
        return 1 if out > 0 else 0
