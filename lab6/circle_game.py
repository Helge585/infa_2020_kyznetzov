import pygame
from pygame.draw import *
from random import randint

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def move_balls(screen, balls, balls_count):
	"""redraw balls considering the screen's parametrs by this plan:
			1. paint all the balls in black color
			2. if current step leaves screen calculate new increment
			3. redraw all the balls with new positions
	   [0] - x, [1] - y, [2] - dx, [3] - dy, [4] - color, [5] - r
	"""
	for i in range(0, balls_count):
		#paint in black
		circle(screen, BLACK, [balls[i][0], balls[i][1]],
				balls[i][5])

		find_x = True		
		while find_x:
			x_step = balls[i][0] + balls[i][2]#current step
			#x leaves the left or x leaves the right
			if x_step <= balls[i][5] or\
			x_step >= width - balls[i][5]:
				balls[i][2] = -balls[i][2]
			else:
				find_x = False
		
		find_y = True
		while find_y:
			y_step = balls[i][1] + balls[i][3]#current step
			#y leaves the top or x leaves the down
			if y_step <= balls[i][5] or\
			y_step >= height - balls[i][5]: 
				balls[i][3] = -balls[i][3]
			else:
				find_y = False 
		#new position
		balls[i][0] += balls[i][2]
		balls[i][1] += balls[i][3]
		#redraw
		circle(screen, balls[i][4], [balls[i][0], balls[i][1]],
				balls[i][5])
		pygame.display.update()

def new_ball():
	"""create a new ball which has has the folowing 
	construct: x, y, dx, dy, color, r
	where x - the x coordinate
		  y - the y coordinate
		  dx - increment of x
		  dy - increment of y
		  color - ball's color
		  r - radius
	"""
	x = randint(0 + max_radius, width - max_radius)
	y = randint(0 + max_radius, height - max_radius)
	r = randint(min_radius, max_radius) 
	if randint(-1, 1) > 0:
		sign = 1
	else:
		sign = -1
	dx = randint(r, 2 * r) * sign
	dy = randint(r, 2 * r) * sign
	color = COLORS[randint(0, 5)]
	circle(screen, color, (x, y), r)
	return [x, y, dx, dy, color, r]

def move_squares(screen, squares, squares_count):
	"""redraw squares considering the screen's parametrs 
	   by this plan:
			1. paint all the squres in black color
			2. if current step leaves screen then 
				drew in another side
			3. redraw all the balls with new positions
	   [0] - x, [1] - y, [2] - vector, [3] - color, 
	   [4] - side_len, [5] - step_count
	"""
	for i in range(0, squares_count):
		sq = squares[i]
		rect(screen, BLACK, (sq[0], sq[1], sq[4], sq[4]))
		if sq[2] == 1:#step right
			if sq[0] + 2 * sq[4] < width:
				sq[0] += sq[4]
			else:
				sq[0] = 0
		elif sq[2] == 2:#step left
			if sq[0] - 2 * sq[4] > 0:
				sq[0] -= sq[4]
			else:
				sq[0] = width - sq[4]
		elif sq[2] == 3:#step top
			if sq[1] - 2 * sq[4] > 0:
				sq[1] -= sq[4]
			else:
				sq[1] = height - sq[4]
		elif sq[2] == 4:#step down
			if sq[1] + 2 * sq[4] < height:
				sq[1] += sq[4]
			else:
				sq[1] = 0
		rect(screen, sq[3], (sq[0], sq[1], sq[4], sq[4]))
		sq[5] -= 1
		if sq[5] == 0:#get new steps and chanhe vector
			sq[5] = randint(min_step, max_step)
			sq[2] = randint(1, 4)

def new_square():
	"""create a new ball which has has the folowing 
	construct: x, y, vector, color, side_len, step_count
	where x - the top x coordinate
		  y - the top y coordinate
		  vector: 
				1 - right
				2 - left
				3 - top
				4 - down
		  color - square's color
	"""
	x = randint(0 + max_radius, width - max_radius)
	y = randint(0 + max_radius, height - max_radius)
	vector = randint(1, 4)
	color = COLORS[randint(0, 5)]
	side_len = randint(min_radius, max_radius)
	step_count = randint(min_step, max_step)
	return [x, y, vector, color, side_len, step_count]

def click(evt, balls, balls_count):
	"""breaks ball if mouse clicked on the ball
	"""
	global count
	for i in range(0, balls_count):
		#distance from mouse click to the ball center
		click_rad = ((evt.pos[0] - balls[i][0])**2 +\
					 (evt.pos[1] - balls[i][1])**2)**(0.5)
		r = balls[i][5]
		if r > click_rad:
			count += 1
			x = balls[i][0]
			y = balls[i][1]
			color = balls[i][4]
			circle(screen, BLACK, (x, y), r)
			mini_rad = r // 2
			circle(screen, color, (x, y), mini_rad)
			circle(screen, color, (x + r, y), mini_rad)
			circle(screen, color, (x - r, y), mini_rad)
			circle(screen, color, (x, y - r), mini_rad)
			circle(screen, color, (x, y + r), mini_rad)
			pygame.display.update()
			clock.tick(BREAK_FPS)
			circle(screen, BLACK, (x, y), mini_rad)
			circle(screen, BLACK, (x + r, y), mini_rad)
			circle(screen, BLACK, (x - r, y), mini_rad)
			circle(screen, BLACK, (x, y - r), mini_rad)
			circle(screen, BLACK, (x, y + r), mini_rad)
			pygame.display.update()
			balls[i] = new_ball()
		
def print_count():
	print(count)

FPS = 6
BREAK_FPS = 3
count = 0
width = 1000
height = 700

max_radius = 100
min_radius = 10
balls_count = 2

min_step = 5
max_step = 15
square_count = 2

pygame.init()
screen = pygame.display.set_mode((width, height))	
clock = pygame.time.Clock()
finished = False

squares = []
balls = []
for i in range(0, balls_count):
	balls.append(new_ball())
	squares.append(new_square())

while not finished:
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			finished = True
		elif event.type == pygame.MOUSEBUTTONDOWN:
			#click(event, balls, balls_count)
			pass
	move_balls(screen, balls, balls_count)
	move_squares(screen, squares, square_count)
	pygame.display.update()

print_count()
pygame.quit()
