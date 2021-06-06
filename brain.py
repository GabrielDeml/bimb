from neuron import Neuron
# from ..dataProcessing.brainInput import brainInput
class Brain:
    neurons = [Neuron]
     
    def get_neuron(self, x : int):
        return self.neurons[x]
    
    def createNeuron(self):
        self.neurons.append(Neuron())
        return len(self.neurons)