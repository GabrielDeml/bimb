# from brain import Brain
import random
import copy
class Being:
    weight = 0;
    bias = 0;

    def mutate(self):
        if bool(random.getrandbits(1)):
            self.weight += (random.random() - 0.5)
        else:
            self.bias += (random.random() - 0.5)

    def test(self, input : int):
        return (self.weight * input) + self.bias 


goal = 1

if __name__ == "__main__":
    print("Welcome to big inteligent machine brain")
    random.seed(1)

    beings = []
    # This is a super simple implementation of the brain I just want to prove that is some what works

    # Generate beings
    for i in range(0, 10000):
        beings.append(Being())

    bestBeing = beings[0]
    bestBeingScore = 100000000000

    # For x generations
    for generation in range(0, 10000):
        # First mutate everything 
        for b in beings:
            b.mutate()
        # Test to find the best of the beings
        for b in beings:    
            tmpScore = abs(b.test(1)) - goal 
            if(tmpScore < bestBeingScore):
                bestBeing = b
                bestBeingScore = tmpScore

        for i in range(0, 10000):
            beings[i] = copy.deepcopy(bestBeing)

    print(bestBeingScore)
                        



    # neuron = Neuron();
