''' 
8 puzzle problem using A Star search-

initial state is a 3x3 grid:
2 8 3
1 6 4
7   5

goal state is also a 3x3 grid:
1 2 3
8   4
7 6 5

There is exactly one blank cell in the grid.
Our aim is to move the cells such that we reach
the goal state in minimum number of steps.

'''

from gridworld import GridWorld
from copy import deepcopy
import time

screen_size = 500
cell_width = 45
cell_height = 45
cell_margin = 5

grid = [[0 for col in range(3)] for row in range(3)]

init = deepcopy(grid)
init[0][0] = 2
init[0][1] = 8
init[0][2] = 3
init[1][0] = 1
init[1][1] = 6
init[1][2] = 4
init[2][0] = 7
init[2][2] = 5

goal = deepcopy(grid)
goal[0][0] = 1
goal[0][1] = 2
goal[0][2] = 3
goal[1][0] = 8
goal[1][2] = 4
goal[2][0] = 7
goal[2][1] = 6
goal[2][2] = 5

gridworld = GridWorld(screen_size,cell_width, cell_height, cell_margin,init, goal, init)

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

def calc_heuristic(grid, goal):
	count = 0
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] != goal[i][j]:
				count += 1

	return count

def is_valid(cell):
	if cell[0] >= 0 and cell[0] < len(grid) and cell[1] >= 0 and cell[1] < len(grid[0]):
		return True
	else:
		return False

def draw_state(state):
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			gridworld.draw_cell([state[i][j], [i, j]]) # [number_on_cell, [x, y]]

def run_a_star(init, goal, cost=1):
	opened = []
	visited = []

	f = calc_heuristic(init, goal) # evaluation function
	g = 0 # cost so far

	opened.append([f, g, init])

	next = opened.pop()
	visited.append(next)
	print "next state is :", next
	while next[2] != goal:

		g = next[1]
		f = next[0]
		# explore the neighborhood!
		for i in range(len(next[2])):
			for j in range(len(next[2][0])):
				# go up, left, down, right
				for a in range(len(delta)):
					x = i + delta[a][0] 
					y = j + delta[a][1]

					# check if this cell--> x, y is a valid cell
					if is_valid([x, y]):
						# now check if this new cell is a zero cell
						if next[2][x][y] == 0:
							next_copy = []
							next_copy = deepcopy(next[2])
							# swap
							next_copy[x][y] = deepcopy(next_copy[i][j])
							next_copy[i][j] = 0

							# check if this new state (entire new_copy grid) is in visited
							if next_copy not in visited:
								g2 = g + cost
								f2 = g2 + calc_heuristic(next_copy, goal)
								opened.append([f2, g2, next_copy])
								visited.append(next_copy)
		opened.sort()
		opened.reverse()

		if len(opened) > 0:
			next = opened.pop()
			print "next state is :",next[2]
			# draw this state on pygame screen
			draw_state(next[2])
			gridworld.update()
			time.sleep(1)


# initial state	
draw_state(init)		

gridworld.update()
time.sleep(1)

run_a_star(init, goal)

