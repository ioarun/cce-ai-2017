'''
Dijkstra's Algorithm for finding the shortest distance.
'''
import copy

# backtracking
def findpath(visited,matrix, size, end):
	path = [end]
	# start from the last row
	j = size-1
	for i in range(size-1,0, -1):
		# compare the cost of the node just above the current node
		# if there is a change, append the corresponding visited node 
		# to the path
		if (matrix[i][j] != matrix[i-1][j]):
			path.append(visited[i-1])
		# if the cost of the node just above the current node is 10000 (infinity),
		# move to the left column for the next iteration
		if matrix[i-1][j] == 10000:
			j -= 1
	return path

def return_index(unseen_nodes,letter):
	i = 0
	for key in unseen_nodes:
		if key == letter:
			return i
		i += 1

def return_index_value(letter):
	return ord(letter) - 65

def return_letter(index):
	return chr(int_index+65)

#graph, start, destination and number of points
def dijkstra(graph, start, end, size):
	print "Original graph :",graph
	# cost matrix ; set all the costs to a large number
	# currently has just one row
	matrix = [[10000 for x in range(size)]]
	matrix_row_counter = 0
	# save start node
	start_temp = start
	# this dictionary will contain key : cost pair
	graph_temp = {}

	# initially all the nodes are unseen
	# the node keys will be popped from unseen_nodes
	# and added in visited_list
	unseen_nodes = graph.keys()
	visited = []

	# all nodes are at really long distances initially
	# so the node values are all set to large number
	for node in unseen_nodes:
		graph_temp.update({node : 10000})

	# start at 'start' node and assign 0 to it
	graph_temp.update({start : 0})

	# first row first column in the cost matrix set to 0
	# eg. [[0, 10000, 10000, 10000]]
	matrix[0][0] = 0
	# add the start node to the visited list
	visited.append(start)
	# remove the source node from the unseen_nodes
	unseen_nodes.pop(return_index(unseen_nodes,start))
	
	while len(unseen_nodes) > 0:

		# a temporary row copies the entries from the previous row of
		# the cost matrix
		temp_row = copy.copy(matrix[matrix_row_counter])

		# child_nodes directly connected to the current node
		# are temporarily added in keys_temp
		keys_temp = []
		for keys, values in zip(graph[start].keys(), graph[start].values()):
			# if child_node is not visited, then only consider
			if keys not in visited:
				# check if source value + path weight < current node value or cost
				if graph_temp[start] + values < graph_temp[keys]:
					# update 
					graph_temp.update({keys : graph_temp[start] + values}) 
				# add the child_nodes
				keys_temp.append(keys)
				# also update the temp_row with the update values
				int_index = return_index_value(keys)
				temp_row[int_index] = graph_temp[keys]

		# assume that the first child has smallest cost
		min_key = keys_temp[0]

		# go through each child node to see which has smaller cost
		# visit the one with minimum cost
		for keys in keys_temp:
			if graph_temp[keys] < graph_temp[min_key]:
				min_key = keys
		
		visited.append(min_key)
		
		# add the temp_row to the cost matrix
		matrix.append(temp_row)
		matrix_row_counter += 1

		# remove the minimum cost node from unseen_nodes
		unseen_nodes.pop(return_index(unseen_nodes,min_key))

		# set start to the minimum cost node
		start = min_key
	
	print "Shortest path is :",findpath(visited,matrix, size, end)

# example graphs
'''
graph = {
	'A' : {'B': 5, 'C': 10},
	'B' : {'A': 5, 'C': 4, 'D': 11},
	'C' : {'A': 10, 'B': 4, 'D': 5},
	'D' : {'B': 11, 'C': 5}
}

'''

'''
graph = {
	'A' : {'B': 4, 'D': 8},
	'B' : {'A': 4, 'C': 3},
	'C' : {'B': 3, 'D': 4},
	'D' : {'C': 4, 'A': 8, 'E': 7},
	'E' : {'D': 7}
}
'''

graph = {
	'A' : {'B': 10, 'C': 5},
	'B' : {'A': 10, 'C': 8, 'E': 6, 'D': 12},
	'C' : {'A': 5, 'B': 8, 'E': 12},
	'D' : {'B': 12, 'E': 5, 'F': 4},
	'E' : {'C': 12, 'B': 6, 'D': 5, 'F': 6},
	'F' : {'D': 4, 'E': 6}
}

dijkstra(graph, 'A', 'F',6)



