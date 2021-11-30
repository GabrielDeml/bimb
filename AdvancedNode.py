import random
import math
import numpy as np


class AdvancedNode:
    '''Advanced mathematical layer. 

    The goal of this layer is to make the network have nothing predefined. Not even how the layer works.
    The only assumptions this layer has is there is a single number input, a single number output, and we can do all basic math operations.


    '''
    possible_operators = ['+', '-', '*', '/']
    varables = []
    operators = []
    parent_nodes = []
    child_nodes = []
    child_mutation_rate = 0.1
    self_mutation_rate = 0.1

    def __init__(self, children=[], varables=None, operators=None, child_mutation_rate=0.1, self_mutation_rate=0.1):
        '''Initialize node'''
        self.child_nodes = children
        self.varables = varables
        self.operators = operators
        self.child_mutation_rate = child_mutation_rate
        self.self_mutation_rate = self_mutation_rate

    def calculate_output(self, data_in):
        '''Run node on input'''
        output = data_in
        if self.varables is not None:
            for i in range(len(self.varables)):
                varable = self.varables[i]
                operator = self.operators[i]
                # if type is np.ndarray:
                
                try:
                    # if data_in is np.ndarray:
                    if type(data_in) is np.ndarray:
                        if operator == '+':
                            output = np.add(output, varable)
                        elif operator == '-':
                            output = np.subtract(output, varable)
                        elif operator == '*':
                            output = np.multiply(output, varable)
                        elif operator == '/':
                            output = np.divide(output, varable)
                    else:
                        if operator == '+':
                            output += varable
                        elif operator == '-':
                            output -= varable
                        elif operator == '*':
                            output *= varable
                        elif operator == '/':
                            output /= varable
                        else:
                            print("Invalid operator")
                except:
                    pass
            return output

    def run_node(self, input_data):
        '''Run node on input'''
        output = 0
        calculated_input = self.calculate_output(input_data)
        if self.child_nodes is None:
            if calculated_input is not None:
                return calculated_input
        else:
            if self.child_nodes is not None:
                if calculated_input is not None:
                    for child_node in self.child_nodes:
                        output += child_node.run_node(calculated_input)
        return output

    def self_mutate(self):
        '''Mutate self'''
        if random.random() < self.self_mutation_rate:
            self.add_varable(random.uniform(-1, 1),
                             random.choice(self.possible_operators))
        if random.random() < self.self_mutation_rate:
            if self.varables is not None:
                i = random.randint(0, len(self.varables))
                try:
                    self.varables.remove(i)
                except:
                    pass

        self.child_mutate()

    def child_mutate(self, depth=0, max_depth=5):
        '''Mutate child nodes'''
        if random.random() < self.child_mutation_rate:
            if random.random() < 0.5 and depth < max_depth:
                self.add_child_node(AdvancedNode())
            else:
                if self.child_nodes is not None and (len(self.child_nodes) > 0):
                    i = random.randint(0, len(self.child_nodes))
                    try:
                        self.child_nodes.pop(i)
                    except:
                        self.child_nodes = None

    def mutate(self, depth=0, max_depth=5):
        # if depth < max_depth:
        self.self_mutate()
        self.child_mutate(depth, max_depth)
        # If self.child_nodes is not empty, mutate each child node
        if self.child_nodes is not None and len(self.child_nodes) > 0:
            for child_node in self.child_nodes:
                child_node.mutate(depth + 1, max_depth)

    def add_child_node(self, node):
        '''Add child node to layer'''
        # TODO: Make child node init with varables and operators
        if self.child_nodes is None:
            self.child_nodes = [node]
        else:
            self.child_nodes.append(node)
        

    def add_varable(self, varable, operator):
        '''Add varable to layer'''
        if self.varables is None:
            self.varables = [varable]
            self.operators = [operator]
        else:
            self.varables.append(varable)
            self.operators.append(operator)
