from neuron import Neuron
# from ..dataProcessing.brainInput import brainInput
class Brain:
    neuronIdCounter = 0
    neurons = {Neuron, int}
     
    def get_neuron(self, x : int):

        return self.neurons[x]
    
    def createNeuron(self):
        self.neurons[self.neuronIdCounter] = Neuron()
        return self.neuronIdCounter + 1