import pygame
from pygame.draw import *

YELLOW = (225, 225, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREY = (80, 80, 80)
GREEN = (0, 255, 0)
BLUE = (0, 0, 200)
BROWN = (65, 43, 21)

pygame.init()

def print_sky(screen, x, y):
	rect(screen, BLUE, (0, 0, x, y // 2))

def print_ground(screen, x, y):
	rect(screen, GREEN, (0, y // 2, x, y // 2))

def print_house(screen, x, y):
	house_width = x // 5
	house_height = x // 5
	base_point = (x // 6, y // 2.5)
	rect(screen, BROWN, (base_point[0], base_point[1],
						house_width, house_height))
	window_width = house_width // 4
	rect(screen, BLUE, (base_point[0] + house_width // 2 -\
						 window_width // 2,
						base_point[1] + house_height // 2 -\
						window_width // 2,
						window_width, window_width))
	polygon(screen, RED, [
	[base_point[0], base_point[1]], 
	[base_point[0] + house_width//2,base_point[1] - house_width//2],
	[base_point[0] + house_width, base_point[1]]
	]) 

def print_tree(screen, x, y):
	bpoint = ((x // 4) * 3, int(y // 2.1))
	tree_high = y // 6
	line(screen, BLACK, [bpoint[0], bpoint[1]],
						[bpoint[0], bpoint[1] + tree_high], 10)
	leaf_rad = tree_high // 3
	kon_rad = leaf_rad + 2
	#centre
	circle(screen, BLACK, (bpoint[0], bpoint[1]-leaf_rad), kon_rad)
	circle(screen, GREEN, (bpoint[0], bpoint[1]-leaf_rad), leaf_rad)
	#top
	circle(screen, BLACK, (bpoint[0],bpoint[1]-3*leaf_rad),kon_rad)
	circle(screen, GREEN, (bpoint[0],bpoint[1]-3*leaf_rad),leaf_rad)
	#left down
	circle(screen, BLACK, (bpoint[0] - leaf_rad,
			bpoint[1] - int(leaf_rad // 1.5)), kon_rad)
	circle(screen, GREEN, (bpoint[0] - leaf_rad,
			bpoint[1] - int(leaf_rad // 1.5)), leaf_rad)
	#left top
	circle(screen, BLACK, (bpoint[0] - int(leaf_rad * 1.3),
				bpoint[1] - 2 * leaf_rad), kon_rad)
	circle(screen, GREEN, (bpoint[0] - int(leaf_rad * 1.3),
				bpoint[1] - 2 * leaf_rad), leaf_rad)
	#right down
	circle(screen, BLACK, (bpoint[0] + leaf_rad,
			bpoint[1] - int(leaf_rad // 1.5)), kon_rad)
	circle(screen, GREEN, (bpoint[0] + leaf_rad,
			bpoint[1] - int(leaf_rad // 1.5)), leaf_rad)
	#rigth top
	circle(screen, BLACK, (bpoint[0] + int(leaf_rad * 1.3),
				bpoint[1] - 2 * leaf_rad), kon_rad)
	circle(screen, GREEN, (bpoint[0] + int(leaf_rad * 1.3),
				bpoint[1] - 2 * leaf_rad), leaf_rad)

def print_cloud(screen, x, y):
	pass

def print_sun(screen, x, y):
	pass

def print_picture(screen, width, height):
	print_sky(screen, width, height)
	print_ground(screen, width, height)
	print_house(screen, width, height)
	print_tree(screen, width, height)
	print_cloud(screen, width, height)
	print_sun(screen, width, height)

FPS = 30
width = 600
height = 400
screen = pygame.display.set_mode((width, height))
screen.fill(BLUE)

print_picture(screen, width, height)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			finished = True

pygame.quit()
