import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1
BREAK_FPS = 3
count = 0
width = 1000
height = 700
max_radius = 100
min_radius = 10
screen = pygame.display.set_mode((width, height))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def new_ball():
	'''рисует новый шарик '''
	global x, y, r, color
	x = randint(0 + max_radius, width - max_radius)
	y = randint(0 + max_radius, height - max_radius)
	r = randint(min_radius, max_radius)
	color = COLORS[randint(0, 5)]
	circle(screen, color, (x, y), r)

def click(evt):
	global count
	click_rad = ((evt.pos[0] - x)**2 + (evt.pos[1] - y)**2)**(0.5)
	if r > click_rad:
		count += 1
		circle(screen, BLACK, (x, y), r)
		mini_rad = r // 2
		circle(screen, color, (x, y), mini_rad)
		circle(screen, color, (x + r, y), mini_rad)
		circle(screen, color, (x - r, y), mini_rad)
		circle(screen, color, (x, y - r), mini_rad)
		circle(screen, color, (x, y + r), mini_rad)
		pygame.display.update()
		clock.tick(BREAK_FPS)
		
def print_count():
	print(count)
	
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			finished = True
		elif event.type == pygame.MOUSEBUTTONDOWN:
			click(event)
	
	new_ball()
	pygame.display.update()
	screen.fill(BLACK)

print_count()
pygame.quit()
