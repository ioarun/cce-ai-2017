'''
A visual demonstration of Breadth First Search Algorithm
using Pygame.
''' 
import pygame
import time
from copy import deepcopy
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# cell dimensions
WIDTH = 45
HEIGHT = 45
MARGIN = 5
 
pygame.init()
pygame.font.init()
 
# Set the width and height of the screen [width, height]
size = (500, 500)
screen = pygame.display.set_mode(size)

font=pygame.font.SysFont('arial', 20)
#text=font.render('@', True, (0, 0, 0))

pygame.display.set_caption("Grid world")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

row = 0
column = 0

init = [0, 0]
goal = [3, 8]
grid = []
policy = []
color = RED

def init_grid(init, goal, obs=0):
    for row in range(10):
        grid.append([])
        policy.append([])
        for column in range(10):
            grid[row].append(0)
            policy[row].append(' ')

    policy[goal[0]][goal[1]] = '*'
    policy[init[0]][init[1]] = 's'

    grid[init[0]][init[1]] = 1  # initial state
    grid[goal[0]][goal[1]] = 10 # goal state

    if obs==1:
        grid[0][5] = -10 # obstacle
        grid[1][5] = -10 # obstacle
        grid[2][5] = -10 # obstacle
        grid[3][5] = -10 # obstacle
        # grid[4][5] = -10 # obstacle
        # grid[5][5] = -10 # obstacle
        # grid[4][6] = -10 # obstacle
        # grid[5][5] = -10 # obstacle
        # grid[6][5] = -10 # obstacle
        # grid[7][5] = -10 # obstacle
        # grid[8][5] = -10 # obstacle
        # grid[9][5] = -10 # obstacle
        

    elif obs==2:
        j = 9
        for i in range(len(grid)):
            grid[i][j] = -10
            j -= 1

    elif obs==3:
        grid[2][3] = -10
        grid[2][6] = -10
        grid[5][2] = -10
        grid[6][3] = -10
        grid[7][4] = -10
        grid[7][5] = -10
        grid[6][6] = -10
        grid[5][7] = -10
    

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
            #rect = text.get_rect()
            #cell_window = pygame.display.set_mode((45, 45))
            #cell_window.blit(text, rect)
            #pygame.display.update()

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def draw_cell(nodes, color):
    for node in nodes:
        row = node[1][0]
        column = node[1][1]
        if node[1] == goal:
            color = RED
        value = node[0]
        rect = pygame.draw.rect(screen, 
            color,
            [(MARGIN + WIDTH) * column + MARGIN,
            (MARGIN + HEIGHT) * row + MARGIN,
            WIDTH,
            HEIGHT])
        TextSurf, TextRect = text_objects(str(value), font)
        TextRect.center = ((MARGIN + WIDTH) * column + 4*MARGIN,(MARGIN + HEIGHT) * row + 4*MARGIN)
        screen.blit(TextSurf, TextRect)
    clock.tick(60)
    pygame.display.flip()

def draw_optimal_path(path, color):
    origin = [0+1*MARGIN+22.5,0+1*MARGIN+22.5]
    col = MARGIN + WIDTH
    row = MARGIN + HEIGHT
    pygame.draw.lines(screen, color, False, [(origin[0]+col*i[1], origin[1]+row*i[0]) for i in path], 4)
    clock.tick(60)
    pygame.display.flip()
    while True:
        pass

def smooth(path, weight_data = 0.5, weight_smooth = 0.1, tolerance = 0.000001):

    # Make a deep copy of path into newpath
    newpath = deepcopy(path)

    change = tolerance

    while change >= tolerance:
        change = 0
        for i in range(1, len(path) - 1):
            for j in range(len(path[0])):
                d1 = weight_data*(path[i][j] - newpath[i][j])
                d2 = weight_smooth*(newpath[i-1][j] + newpath[i+1][j] - 2*newpath[i][j])
                change += abs(d1 + d2)
                newpath[i][j] += d1 + d2
                
    
    return newpath 
      

def check_valid(node):
    if node[0] >= 0 and node[0] < len(grid) and node[1] >= 0  and node[1] < len(grid[0]) and (grid[node[0]][node[1]] == 0 or grid[node[0]][node[1]] == 10):
        return True
    else:
        return False

def run_bfs(init, goal, grid,cost):
    flag = False
    delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 0, 1 ], # go down
         [ 1, 0 ]] # go right
    delta_name = ['^', '<', 'v', '>']
    action = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]

    next = None
    visited = []
    opened = []
    opened.append([0, init])
    visited.append(init)
    opened.sort()
    opened.reverse()
    next = opened.pop()
    came_from = []
    while next[1]!= goal:
        #print opened
        #draw_cell(next[1], YELLOW)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print "Mouse button pressed"
                flag = True
                # pos = pygame.mouse.get_pos()
                # column = pos[0] // (WIDTH + MARGIN)
                # row = pos[1] // (WIDTH + MARGIN)
                # print("Click ", pos, "Grid coordinates: ", row, column)
                # grid[row][column] = 1
        temp = []
        print "expanding node :",next[1]
        print "neighboring nodes: "
        for d in range(len(delta)):
            x = next[1][0] + delta[d][0]
            y = next[1][1] + delta[d][1]

            if check_valid([x, y]):
                if [x, y] not in visited:
                    #print "at :",[next[1][0], next[1][1]],"taking step :",d
                    opened.append([next[0]+cost, [x, y]])
                    #print "appending ",[x, y]
                    #print opened
                    visited.append([x, y])
                    temp.append([next[0]+cost, [x, y]])
                    # if next[1] != init:
                    #     policy[next[1][0]][next[1][1]] = delta_name[d]
                    action[x][y] = d
                    # print "adjacent uncovered nodes: ", [x, y]
                    #draw_cell([x, y], BLUE)
                    #print "Expanding :",[x, y]
                    # time.sleep(0.5)
                    # # Limit to 60 frames per second
                    # clock.tick(60)
                    # # update the screen with what we've drawn.
                    # pygame.display.flip()
        print temp
        draw_cell(temp, BLUE)
        time.sleep(0.1)
        # opened.sort()
        # opened.reverse()
        if(len(opened)>0):
            next = opened.pop(0)
            #print next

    # policy search
    x = goal[0]
    y = goal[1]
    policy[x][y] = '*'
    path = []
    path.append([x, y])
    while([x, y] != init):
        x1 = x - delta[action[x][y]][0]
        y1 = y - delta[action[x][y]][1]
        policy[x1][y1] = delta_name[action[x][y]]
        x = x1
        y = y1
        path.append([x, y])
    print policy
    path.reverse()
    draw_optimal_path(smooth(path), GREEN)
    #print visited
init_grid(init, goal, obs=1)
run_bfs(init, goal, grid, cost=1)
# Close the window and quit.
pygame.quit()
