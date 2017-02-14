'''
A visual demonstration of Breadth First Search Algorithm
using Pygame.
''' 
import pygame
import time
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# cell dimensions
WIDTH = 45
HEIGHT = 45
MARGIN = 5
 
pygame.init()
pygame.font.init()
 
# Set the width and height of the screen [width, height]
size = (500, 500)
screen = pygame.display.set_mode(size)

# font=pygame.font.SysFont('arial', 20)
# text=font.render('@', True, (0, 0, 0))

pygame.display.set_caption("Grid world")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

row = 0
column = 0

init = [0, 4]
goal = [9, 9]
grid = []
color = RED

def init_grid():
    for row in range(10):
        grid.append([])
        for column in range(10):
            grid[row].append(0)

    grid[init[0]][init[1]] = 1  # initial state
    grid[goal[0]][goal[1]] = 10 # goal state
    # grid[0][5] = -10 # obstacle
    # grid[1][5] = -10 # obstacle
    # grid[2][5] = -10 # obstacle
    # grid[3][5] = -10 # obstacle
    # grid[4][5] = -10 # obstacle
    # grid[5][5] = -10 # obstacle
    # grid[4][6] = -10 # obstacle
    # grid[5][5] = -10 # obstacle
    # grid[6][5] = -10 # obstacle
    # grid[7][5] = -10 # obstacle
    # grid[8][5] = -10 # obstacle
    # grid[9][5] = -10 # obstacle

    screen.fill(BLACK)

    for row in range(10):
        for column in range(10):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
            elif grid[row][column] == 10:
                color = RED
            elif grid[row][column] == -10:
                color = BLACK
            pygame.draw.rect(screen, 
                color,
                [(MARGIN + WIDTH) * column + MARGIN,
                (MARGIN + HEIGHT) * row + MARGIN,
                WIDTH,
                HEIGHT])
            rect = text.get_rect()
            #cell_window = pygame.display.set_mode((45, 45))
            #cell_window.blit(text, rect)
            #pygame.display.update()


def draw_cell(node, value):
    row = node[0]
    column = node[1]

    pygame.draw.rect(screen, 
            color,
            [(MARGIN + WIDTH) * column + MARGIN,
            (MARGIN + HEIGHT) * row + MARGIN,
            WIDTH,
            HEIGHT])

def check_valid(node):
    if node[0] >= 0 and node[0] < len(grid) and node[1] >= 0  and node[1] < len(grid[0]) and grid[node[0]][node[1]] == 0:
        return True
    else:
        return False

def run_bfs(init, goal, grid,cost):
    color = RED
    flag = False
    delta = [[-1, 0], # up
            [1, 0], # down
            [0, -1], # left
            [0, 1]] # right
    next = None
    visited = []
    opened = []
    opened.append([0, init])
    visited.append(init)
    opened.sort()
    opened.reverse()
    next = opened.pop()
    while next[1]!=goal:
        print next
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print "Mouse button pressed"
                # pos = pygame.mouse.get_pos()
                # column = pos[0] // (WIDTH + MARGIN)
                # row = pos[1] // (WIDTH + MARGIN)
                # print("Click ", pos, "Grid coordinates: ", row, column)
                # grid[row][column] = 1

        for d in range(len(delta)):
            x = next[1][0] + delta[d][0]
            y = next[1][1] + delta[d][1]
            if check_valid([x, y]):
                if [x, y] not in visited:
                    opened.append([next[0]+cost, [x, y]])
                    visited.append([x, y])
                    draw_cell([x, y], next[0]+cost)
                    time.sleep(0.25)
                    # Limit to 60 frames per second
                    clock.tick(60)
                    # update the screen with what we've drawn.
                    pygame.display.flip()
        opened.sort()
        opened.reverse()
        if(len(opened)>0):
            next = opened.pop()

init_grid()

run_bfs(init, goal, grid, cost=1)
# Close the window and quit.
pygame.quit()
