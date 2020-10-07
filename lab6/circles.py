import pygame
from pygame.draw import *
pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

RED = (255, 0, 0)
GREEN = (0, 255, 0)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			finished = True
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				circle(screen, RED, event.pos, 50)
				pygame.display.update()
			elif event.button == 3:
				circle(screen, GREEN, event.pos, 50)
				pygame.display.update()

pygame.quit()
