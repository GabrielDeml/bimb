import copy
from AdvancedNode import AdvancedNode as AN

if __name__ == "__main__":
    # Create root node
    rootNode = AN()
    # For each generation
    for i in range(10):
        # For each being in the generation
        # best score starts as infinity
        bestBeing = AN()
        bestScore = float("inf")
        overallBestBeing = AN()
        overallBestScore = float("inf")
        for j in range(100):
            # Deep copy root node

            tmp_node = copy.deepcopy(rootNode)
            tmp_node.mutate()
            output = tmp_node.run_node(2)
            output = abs(output - 4)
            print("Score: " + str(output))
            if output <= bestScore:
                bestScore = output
                bestBeing = copy.deepcopy(tmp_node)
                print(str(output))
            rootNode = bestBeing
            if output <= overallBestScore:
                overallBestScore = output
                overallBestBeing = copy.deepcopy(tmp_node)
                print(str(output))
            print("Best score: " + str(bestScore))
    print("Overall best score: " + str(overallBestScore))
