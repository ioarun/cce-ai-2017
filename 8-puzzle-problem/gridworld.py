import pygame
import time
from copy import deepcopy

class GridWorld:

	def __init__(self, screen_size,cell_width, 
		cell_height, cell_margin,init, goal, grid):

		# define colors
		self.BLACK = (0, 0, 0)
		self.WHITE = (255, 255, 255)
		self.GREEN = (0, 255, 0)
		self.RED = (255, 0, 0)
		self.BLUE = (0, 0, 255)
		self.YELLOW = (255, 255, 0)

		# cell dimensions
		self.WIDTH = cell_width
		self.HEIGHT = cell_height
		self.MARGIN = cell_margin
		self.color = self.WHITE

		# adjust the grid in the center of screen
		# self.adjust_margin = 75


		pygame.init()
		pygame.font.init()

		# set the width and height of the screen (width , height)
		self.size = (screen_size, screen_size)
		self.screen = pygame.display.set_mode(self.size)

		self.font = pygame.font.SysFont('arial', 20)

		pygame.display.set_caption("Grid world")

		self.clock = pygame.time.Clock()

		self.init = init
		self.goal = goal
		self.grid = grid


		self.screen.fill(self.BLACK)

		for row in range(len(grid)):
			for col in range(len(grid[0])):
				if self.init[row][col] != 0:
					self.color = self.RED
				else:
					self.color = self.WHITE

				pygame.draw.rect(self.screen,
					self.color,
					[(self.MARGIN + self.WIDTH )*col+self.MARGIN,
					(self.MARGIN + self.HEIGHT )*row+self.MARGIN,
					self.WIDTH,
					self.HEIGHT])

	def text_objects(self, text, font):
		textSurface = font.render(text, True, self.BLACK)
		return textSurface, textSurface.get_rect()

	def draw_cell(self, cell):
	
		row = cell[1][0]
		column = cell[1][1]
		number = cell[0]
		if number != 0:
			rect = pygame.draw.rect(self.screen,
				self.RED,
				[(self.MARGIN + self.WIDTH)*column+self.MARGIN,
				(self.MARGIN + self.HEIGHT)*row+self.MARGIN,
				self.WIDTH,
				self.HEIGHT])
			TextSurf, TextRect = self.text_objects(str(number), self.font)
			TextRect.center = ((self.MARGIN + self.WIDTH)*column + 4*self.MARGIN,
				(self.MARGIN + self.HEIGHT)*row + 4*self.MARGIN)
			self.screen.blit(TextSurf, TextRect)
		else:
			rect = pygame.draw.rect(self.screen,
				self.WHITE,
				[(self.MARGIN + self.WIDTH)*column+self.MARGIN,
				(self.MARGIN + self.HEIGHT)*row+self.MARGIN,
				self.WIDTH,
				self.HEIGHT])

	def update(self):
		pygame.display.update()

				









