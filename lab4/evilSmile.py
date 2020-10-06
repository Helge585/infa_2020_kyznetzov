import pygame
from pygame.draw import *

pygame.init()

YELLOW = (225, 225, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREY = (80, 80, 80)

def print_evil_smile(x, y, radius, screen):
	left_radius = int(radius * 0.2)
	right_radius = int(radius * 0.15)

	circle(screen, YELLOW, (x, y), radius)
	
	circle(screen, RED, (x - radius // 2, y - radius // 4),
							left_radius)
	circle(screen, BLACK, (x - radius // 2, y - radius // 4),
							left_radius // 2)
	
	circle(screen, RED, (x + radius // 2, y - radius // 4),
							right_radius)
	circle(screen, BLACK, (x + radius // 2, y - radius // 4),
							right_radius // 2)

	x1 = x - radius // 2 + left_radius + left_radius // 2
	y1 = y - radius // 4 - left_radius // 2
	x2 = x - radius
	y2 = y - radius
	line(screen, BLACK, [x1, y1], [x2, y2], 20)

	x1 = x + radius // 2 - right_radius - right_radius // 2
	y1 = y - radius // 4 - right_radius // 2
	x2 = x + radius
	y2 = y - radius
	line(screen, BLACK, [x1, y1], [x2, y2], 20)

	x1 = x - radius // 2
	y1 = y + radius // 2
	x2 = x + radius // 2
	y2 = y + radius // 2
	line(screen, BLACK, [x1, y1], [x2, y2], 25)

FPS = 30
width = 400
height = 400
screen = pygame.display.set_mode((width, height))
screen.fill(GREY)

print_evil_smile(width // 2, height // 2, 100, screen)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			finished = True

pygame.quit()
