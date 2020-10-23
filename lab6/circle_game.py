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

#main constans
FPS = 4
BREAK_FPS = 3
WIDTH = 1000
HEIGHT = 700
#ball's constans
MAX_RADIUS = 50
MIN_RADIUS = 10
BALLS_COUNT = 2
#square's constants
MIN_STEP = 5
MAX_STEP = 15
SQUARES_COUNT = 2


def move_balls(screen, balls):
	"""redraws balls considering the screen's parametrs 
	   by this plan:
			1. paint all the balls in black color
			2. if current step leaves screen calculate new increment
			3. redraw all the balls with new positions
	   [0] - x, [1] - y, [2] - dx, [3] - dy, [4] - color, [5] - r
	"""
	for i in range(0, BALLS_COUNT):
		#paint in black
		circle(screen, BLACK, [balls[i][0], balls[i][1]],
				balls[i][5])

		find_x = True		
		while find_x:
			x_step = balls[i][0] + balls[i][2]#current step
			#x leaves the left or x leaves the right
			if x_step <= balls[i][5] or\
			x_step >= WIDTH - balls[i][5]:
				balls[i][2] = -balls[i][2]
			else:
				find_x = False
		
		find_y = True
		while find_y:
			y_step = balls[i][1] + balls[i][3]#current step
			#y leaves the top or x leaves the down
			if y_step <= balls[i][5] or\
			y_step >= HEIGHT - balls[i][5]: 
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
	"""creates a new ball which has the folowing 
	construct: x, y, dx, dy, color, r
	where x - the x coordinate
		  y - the y coordinate
		  dx - increment of x
		  dy - increment of y
		  color - ball's color
		  r - radius
	"""
	x = randint(0 + MAX_RADIUS, WIDTH - MAX_RADIUS)
	y = randint(0 + MAX_RADIUS, HEIGHT - MAX_RADIUS)
	r = randint(MIN_RADIUS, MAX_RADIUS) 
	if randint(-1, 1) > 0:
		sign = 1
	else:
		sign = -1
	dx = randint(r, 2 * r) * sign
	dy = randint(r, 2 * r) * sign
	color = COLORS[randint(0, 5)]
	circle(screen, color, (x, y), r)
	return [x, y, dx, dy, color, r]

def move_squares(screen, squares):
	"""redraws squares considering the screen's parametrs 
	   by this plan:
			1. paint all the squres in black color
			2. if current step leaves screen then 
				drew in another side
			3. redraw all the balls with new positions
	   [0] - x, [1] - y, [2] - vector, [3] - color, 
	   [4] - side_len, [5] - step_count
	"""
	for i in range(0, SQUARES_COUNT):
		sq = squares[i]
		rect(screen, BLACK, (sq[0], sq[1], sq[4], sq[4]))
		if sq[2] == 1:#step right
			if sq[0] + 2 * sq[4] < WIDTH:
				sq[0] += sq[4]
			else:
				sq[0] = 0
		elif sq[2] == 2:#step left
			if sq[0] - 2 * sq[4] > 0:
				sq[0] -= sq[4]
			else:
				sq[0] = WIDTH - sq[4]
		elif sq[2] == 3:#step top
			if sq[1] - 2 * sq[4] > 0:
				sq[1] -= sq[4]
			else:
				sq[1] = HEIGHT - sq[4]
		elif sq[2] == 4:#step down
			if sq[1] + 2 * sq[4] < HEIGHT:
				sq[1] += sq[4]
			else:
				sq[1] = 0
		rect(screen, sq[3], (sq[0], sq[1], sq[4], sq[4]))
		sq[5] -= 1
		if sq[5] == 0:#get new steps and chanhe vector
			sq[5] = randint(MIN_STEP, MAX_STEP)
			sq[2] = randint(1, 4)

def new_square():
	"""creates a new ball which has the folowing 
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
	x = randint(MAX_RADIUS, WIDTH - MAX_RADIUS)
	y = randint(MAX_RADIUS, HEIGHT - MAX_RADIUS)
	vector = randint(1, 4)
	color = COLORS[randint(0, 5)]
	side_len = randint(MIN_RADIUS, MAX_RADIUS)
	step_count = randint(MIN_STEP, MAX_STEP)
	return [x, y, vector, color, side_len, step_count]

def check_balls(screen, evt, balls):
	"""breaks ball if mouse clicked on the ball
	   returns hit count
	"""
	count = 0
	for i in range(0, BALLS_COUNT):
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
			#breaks circle
			circle(screen, color, (x, y), mini_rad)
			circle(screen, color, (x + r, y), mini_rad)
			circle(screen, color, (x - r, y), mini_rad)
			circle(screen, color, (x, y - r), mini_rad)
			circle(screen, color, (x, y + r), mini_rad)
			pygame.display.update()
			clock.tick(BREAK_FPS)
			#deletes circle
			circle(screen, BLACK, (x, y), mini_rad)
			circle(screen, BLACK, (x + r, y), mini_rad)
			circle(screen, BLACK, (x - r, y), mini_rad)
			circle(screen, BLACK, (x, y - r), mini_rad)
			circle(screen, BLACK, (x, y + r), mini_rad)
			pygame.display.update()
			balls[i] = new_ball()
	return count

def check_squares(screen, evt, squares):
	"""breaks square if mouse clicked on the sqaure
	   returns hit count
	   [0] - x, [1] - y, [4] - side_len
	"""
	sq = squares
	count = 0
	for i in range(0, SQUARES_COUNT):	
		#if click x in (x, x + side_len) and 
		#click y in (y, y + side_len)
		if evt.pos[0] > sq[i][0]\
		and evt.pos[0] < sq[i][0] + sq[i][4]\
		and evt.pos[1] > sq[i][1]\
		and evt.pos[1] < sq[i][1] + sq[i][4]:
			count += 2
			rect(screen, BLACK, (sq[i][0], sq[i][1], sq[i][4], 
				sq[i][4]))
			mini_side = sq[i][4] // 3
			color = sq[i][3]
			#breaks square
			rect(screen, color, (sq[i][0], sq[i][1], mini_side,
				mini_side))
			rect(screen, color, (sq[i][0] + sq[i][4], 
				sq[i][1], mini_side, mini_side))
			rect(screen, color, (sq[i][0], sq[i][1] + sq[i][4], 
				mini_side, mini_side))
			rect(screen, color, (sq[i][0] + sq[i][4], 
				sq[i][1] + sq[i][4], mini_side, mini_side))
			pygame.display.update()
			clock.tick(BREAK_FPS)
			#deletes square
			rect(screen, BLACK, (sq[i][0], sq[i][1], mini_side,
				mini_side))
			rect(screen, BLACK, (sq[i][0] + sq[i][4], 
				sq[i][1], mini_side, mini_side))
			rect(screen, BLACK, (sq[i][0], sq[i][1] + sq[i][4], 
				mini_side, mini_side))
			rect(screen, BLACK, (sq[i][0] + sq[i][4], 
				sq[i][1] + sq[i][4], mini_side, mini_side))
			pygame.display.update()
			sq[i] = new_square()
	return count
			
def click(screen, evt, balls, squares):
	"""returns ball's and square's hit counts"""
	return check_balls(screen, evt, balls) +\
 			check_squares(screen, evt, squares)
	

def get_name(screen, clock):
	"""reads player name and returns it"""
	name = ""
	start_str = "Write your name or enter for exit"
	name_str = ">>> "
	x_str = WIDTH // 3
	y_str = HEIGHT // 3	
	font_size = 30
	
	myfont = pygame.font.SysFont("serif", font_size)
	
	textsurface = myfont.render(start_str, False, BLUE)
	screen.blit(textsurface,(x_str, y_str))
	
	textsurface = myfont.render(name_str, False, BLUE)
	screen.blit(textsurface,(x_str, y_str + 30))
	pygame.display.update()

	finished = False
	while not finished:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.__dict__["unicode"] == u"\n" or\
				event.__dict__["unicode"] == u"\r" :
					finished = True
				#if backspace and input isn't empty
				elif event.__dict__["unicode"] == u"\b" and\
				len(name_str) > 4:
					#paint old input in black
					textsurface = myfont.render(name_str, 
												False, BLACK)
					screen.blit(textsurface,(x_str, y_str + 30))
					#delete one symbol
					name_str = name_str[:-1]
					#paint new input
					textsurface = myfont.render(name_str, 
												False, BLUE)
					screen.blit(textsurface,(x_str, y_str + 30))
					pygame.display.update()
				#add new symbol in input
				else:
					name_str += event.__dict__["unicode"]
					textsurface = myfont.render(name_str, 
												False, BLUE)
					screen.blit(textsurface,(x_str, y_str + 30))
					pygame.display.update()
	
	return name_str[4:]
	
	
def start_game():
	"""game cicle, returns hit count"""
	count = 0
	squares = []
	balls = []
	for i in range(0, BALLS_COUNT):
		balls.append(new_ball())
		squares.append(new_square())
	finished = False
	while not finished:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				finished = True
			elif event.type == pygame.MOUSEBUTTONDOWN:
				count += click(screen, event, balls, squares)
		move_balls(screen, balls)
		move_squares(screen, squares)
		pygame.display.update()
	return count

def record_result(result):
	"""records best results in file"""
	table_count = 3
	try:
		output_file = open("results.txt", mode = "r")
	except OSError:
		pass
	#current minimum
	min_res = min(result)[0]
	#reads file's results > current minimum 
	#and adds them in current result list
	line = output_file.readline()
	#print(line)
	#return
	while line != "":
		count, name = line.split(" ")
		if int(count) < min_res:
			break
		result.append([count, name])
		line = output_file.readline()
	output_file.close()
	#sorts and writes the best players in file
	result.sort(key = lambda res: res[0], reverse = True)
	input_file = open("results.txt", mode = "w")
	for i in range(0, min(table_count, len(result))):
		input_file.write(str(result[i][0]) + " " + 
							result[i][1] + "\r")
	input_file.close()



pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))	
clock = pygame.time.Clock()
result = []
#main cicle
name = get_name(screen, clock)
while len(name) > 0:
	screen.fill(BLACK)
	pygame.display.update()
	count = start_game()
	result.append([count, name])
	screen.fill(BLACK)
	pygame.display.update()
	name = get_name(screen, clock)

#print(result)
record_result(result)
pygame.quit()



























