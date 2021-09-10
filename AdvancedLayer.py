import math
class AdvancedLayer:
	'''Advanced mathematical layer. 

	The goal of this layer is to make the network have nothing predefined. Not even how the layer works.
	The only assumptions this layer has is there is a single number input, a single number output, and we can do all basic math operations.
	
	
	'''
	varables = []
	operators = []


	def run_on_input(self, data_in):
		'''Run layer on input'''
		output = data_in
		for i in range(len(self.varables)):
			varable = self.varables[i]
			operator = self.operators[i]
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
			elif operator == '!':
				output = math.factorial(output)
			else:
				print("Invalid operator")
		return output

	def add_varable(self, varable, operator):
		'''Add varable to layer'''
		self.varables.append(varable)
		self.operators.append(operator)
			
			