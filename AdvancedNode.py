import random
import math


class AdvancedNode:
    '''Advanced mathematical layer. 

    The goal of this layer is to make the network have nothing predefined. Not even how the layer works.
    The only assumptions this layer has is there is a single number input, a single number output, and we can do all basic math operations.


    '''
    possible_operators = ['+', '-', '*', '/',
                          '^', '%', 's', 'c', 't', 'l', 'e']
    varables = []
    operators = []
    parent_nodes = []
    child_nodes = []
    child_mutation_rate = 0.1
    self_mutation_rate = 0.1

    def __init__(self, children=None, varables=None, operators=None, child_mutation_rate=0.1, self_mutation_rate=0.1):
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
                try:
                    if operator == '+':
                        output += varable
                    elif operator == '-':
                        output -= varable
                    elif operator == '*':
                        output *= varable
                    elif operator == '/':
                        output /= varable
                    elif operator == '^':
                        output **= varable
                    elif operator == '%':
                        output %= varable
                    elif operator == 's':
                        output = math.sqrt(output)
                    elif operator == 's':
                        output = math.sin(output)
                    elif operator == 'c':
                        output = math.cos(output)
                    elif operator == 't':
                        output = math.tan(output)
                    elif operator == 'l':
                        output = math.log(output)
                    elif operator == 'e':
                        output = math.exp(output)
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

    def child_mutate(self):
        '''Mutate child nodes'''
        if random.random() < self.child_mutation_rate:
            self.add_child_node(AdvancedNode())

    def mutate(self):
        self.self_mutate()
        self.child_mutate()
        if self.child_nodes is not None:
            for child_node in self.child_nodes:
                child_node.mutate()

    def add_child_node(self, node):
        '''Add child node to layer'''
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
