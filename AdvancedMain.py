from AdvancedNode import AdvancedNode as AN

if __name__ == "__main__":
	# Create root node
	rootNode = AN()
	for i in range(1000):
		rootNode.mutate()
		output = rootNode.run_node(1)
		print(str(output))

