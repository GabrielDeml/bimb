class Neuron:

    weight = 0
    bias = 0
    children = []

    def __init__(self):
        print("You created a neuron")


    def computeNeuron(self, x: int) -> int:
        for child in self.children:
            
            (x * self.weight) + self.bias
            return
