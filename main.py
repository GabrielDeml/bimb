# from brain import Brain
import random
import copy
class Being:
    weight = 0;
    bias = 0;

    def mutate(self):
        if bool(random.getrandbits(1)):
            self.weight += (random.random() - 0.5)/1000000000
        else:
            self.bias += (random.random() - 0.5)/10000000

    def test(self, input):
        return (self.weight * input) + self.bias 


goal = 1

number_of_generations = 100
# TODO: Add me in
number_of_beings = 100
if __name__ == "__main__":
    print("Welcome to big inteligent machine brain")
    random.seed(1)

    beings = []
    # This is a super simple implementation of the brain I just want to prove that is some what works

    # Generate beings
    for i in range(0, number_of_generations):
        beings.append(Being())

    bestBeing = beings[0]
    bestBeingScore = 100000000000

    # For x generations
    for generation in range(0, number_of_generations):
        # First mutate everything 
        for b in beings:
            b.mutate()
        # Test to find the best of the beings
        for b in beings:    
            tmpScore = abs(b.test(1)) - goal 
            # The optimization algorithm is messed up
            if(tmpScore < bestBeingScore):
                bestBeing = b
                bestBeingScore = tmpScore

        for i in range(0, number_of_generations):
            beings[i] = copy.deepcopy(bestBeing)

    print(bestBeingScore)