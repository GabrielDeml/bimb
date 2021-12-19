import copy
from random import Random, randint
from AdvancedNode import AdvancedNode as AN
import gc

if __name__ == "__main__":
    # Create root node
    rootNode = AN()
    # For each generation
    overallBestBeing = AN()
    overallBestScore = float("inf")
    testNumber = 0

    # Create 100 tests
    testArray = []
    for i in range(100):
        testArray.append(randint(1, 100))


    for i in range(10000):
        # For each being in the generation
        # best score starts as infinity
        bestBeing = AN()
        bestScore = float("inf")
        for j in range(100):
            output = 0
            tmp_node = copy.deepcopy(rootNode)
            tmp_node.mutate()
                
            for rand in testArray:
                # Deep copy root node
                output = tmp_node.run_node(rand)
                #TODO: Run multiple tests
                output += abs(output - (rand ** 2))
                # print("Score: " + str(output))
            if output <= bestScore:
                bestScore = output
                bestBeing = copy.deepcopy(tmp_node)
                # print(str(output))
            if output <= overallBestScore:
                testNumber = rand
                overallBestScore = output
                overallBestBeing = copy.deepcopy(tmp_node)
        rootNode = bestBeing
        print("Best score: " + str(bestScore))
    print("Overall best score: " + str(overallBestScore))
    print("Overall best being test number: " + str(testNumber))
    print("Overall best being: " + str(overallBestBeing))
    print("Variables: " + str(overallBestBeing.getVariables()))
    print("Operators: " + str(overallBestBeing.getOperators()))
