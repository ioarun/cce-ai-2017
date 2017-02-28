''' 
N puzzle problem using A Star search-

initial state is a NxN grid.

goal state is also a NxN grid.

There is exactly one blank cell in the grid.
Our aim is to move the cells such that we reach
the goal state in minimum number of steps.

'''

from gridworld import GridWorld
from copy import deepcopy
import time
import random
import pygame


screen_size = 500
cell_width = 45
cell_height = 45
cell_margin = 5

grid = [[0 for col in range(4)] for row in range(4)]

# add numbers from 0 to 99 to a list and then shuffle it
numbers_list = [i for i in range(len(grid)*len(grid[0]))]

random.shuffle(numbers_list)

init = deepcopy(grid)
k = 0
for i in range(len(grid)):
	for j in range(len(grid[0])):
		print k
		init[i][j] = numbers_list[k]
		k += 1

# shuffle again to generate goal state
random.shuffle(numbers_list)

goal = deepcopy(grid)
k = 0
for i in range(len(grid)):
	for j in range(len(grid[0])):
		goal[i][j] = numbers_list[k]
		k += 1

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


def run_a_star(init, goal,cost=1):
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
							next_copy[x][y] = (next_copy[i][j])
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
			time.sleep(3)

# initial state	
draw_state(init)		

gridworld.update()

run_a_star(init, goal)

