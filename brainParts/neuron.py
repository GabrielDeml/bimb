class Neuron:

    weight = 0
    bias = 0

    def __init__(self):
        print("You created a neuron")


    def computeNeuron(self, x: int) -> int:
        return (x * self.weight) + self.bias
