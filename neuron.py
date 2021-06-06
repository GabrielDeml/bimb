from brain import Brain
class Neuron:

    weight = 0
    bias = 0
    children = [int]
    parents = [int]

    def __init__(self, brain : Brain):
        print("You created a neuron")


    def computeNeuron(self, x: int) -> int:
        # for child in self.children:
        for parent in self.parents:
            out = (parent.get_data * self.weight) + self.bias
            # return
