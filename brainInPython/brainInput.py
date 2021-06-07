### The direct input into the brain
from neuron import Neuron
class brainInput:
    data = [None]

    def __init__(self, data : list):
        self.data = data

    def get_data(self, x : int):
        return self.data[x]
   