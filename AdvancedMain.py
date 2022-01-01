import copy
from random import Random, randint
from typing import Text

from numpy.typing import _128Bit
from AdvancedNode import AdvancedNode as AN
import multiprocessing
from multiprocessing import Process, Value, Array, Pool


def run_generation(testArray):
    rootNode = AN()
    bestBeing = rootNode
    bestScore = float("inf")
    for generationNumber in range(100):
        # For each being in the generation
        # best score starts as infinity
        tmp_node = copy.deepcopy(rootNode)
        tmp_node.mutate()
        output = 0
        for testIterationCount in range(len(testArray)):
            randomNumber = testArray[testIterationCount]
            output_tmp = tmp_node.run_node(randomNumber)
            output += abs(output_tmp - (randomNumber ** 2))
        outputAvg = output / len(testArray)
        if outputAvg < bestScore:
            bestScore = outputAvg
            bestBeing = tmp_node
        rootNode = bestBeing
    return bestBeing, bestScore

if __name__ == "__main__":
    # Create root node
    
    # For each generation
    overallBestBeing = AN()
    overallBestScore = float("inf")
    testNumber = 0

    # Create 100 tests
    testArray = []
    for i in range(100):
        testArray.append(randint(1, 100))
    
    # Get the number of cpu cores
    num_cores = multiprocessing.cpu_count()
    print("Number of cores: " + str(num_cores))
    # Create worker for each thread
    generations = [(testArray, AN()) for i in range(1000000000)]
    pool = Pool(num_cores)
    # Run the generation
    results = pool.map(run_generation, generations)
    print(results)
    
    # for core in range(num_cores):
    #     numberOfGenerationsTheading = Value('i', 1000000)

    #     # Create a process for each core
    #     p = Process(target=run_generation, args=(testArray))
    #     p.start()
    #     p.join()

    # Find the best being
    for result in results:
        if result[1] < overallBestScore:
            overallBestScore = result[1]
            overallBestBeing = result[0]

    print("Overall best score: " + str(overallBestScore))
    # print("Overall best being test number: " + str(testNumber))
    print("Overall best being: " + str(overallBestBeing))
    # try:
    #     print("Number of child nodes on root: " + str(len(overallBestBeing.child_nodes)))
    # except:
    #     pass
    print("Overall best being children: " + str(overallBestBeing.printOperators()))
    # print("Variables: " + str(overallBestBeing.getVariables()))
    # print("Operators: " + str(overallBestBeing.getOperators()))
