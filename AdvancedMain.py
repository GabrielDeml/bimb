import copy
from random import Random, randint
from AdvancedNode import AdvancedNode as AN
import gc

if __name__ == "__main__":
    # Create root node
    rootNode = AN()
    # For each generation
    for i in range(100):
        # For each being in the generation
        # best score starts as infinity
        bestBeing = AN()
        bestScore = float("inf")
        overallBestBeing = AN()
        overallBestScore = float("inf")
        # Get a random number between 1 and 100
        rand = float(randint(1, 100))
        for j in range(100):
            # Deep copy root node
            tmp_node = copy.deepcopy(rootNode)
            tmp_node.mutate()
            output = tmp_node.run_node(rand)
            output = abs(output - (rand ** 2))
            # print("Score: " + str(output))
            if output <= bestScore:
                bestScore = output
                bestBeing = copy.deepcopy(tmp_node)
                # print(str(output))
                if output <= overallBestScore:
                    overallBestScore = output
                    overallBestBeing = copy.deepcopy(tmp_node)
            else: 
                del tmp_node
                gc.collect()
        rootNode = bestBeing
        print("Best score: " + str(bestScore))
    print("Overall best score: " + str(overallBestScore))
