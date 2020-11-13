from random import randrange as rnd, choice
from abc import ABC, abstractmethod
import tkinter as tk
import math
import time

class Bullet(ABC):
	def __init__(self):
		pass

	@abstractmethod
	def move(self):
		pass

	@abstractmethod
	def hide(self):
		pass

class BallBullet(Bullet):
	def __init__(self, base_x, base_y, dx, dy, width, height, canvas):
# Fix radius and color initializaton
		self.rad = 5
		self.color = 'green'
		self.base_x = base_x
		self.base_y = base_y
		self.dx = dx * self.rad
		self.dy = dy * self.rad
		self.right_side_x = width
		self.back_side_y = height
		self.canvas = canvas
		self.id = self.id = self.canvas.create_oval(
			self.base_x - self.rad,
			self.base_y - self.rad,
			self.base_x + self.rad,
			self.base_y + self.rad,
			fill=self.color
        )

	def move(self):
		self.base_x += self.dx
		self.base_y += self.dy
		if self.base_x < 0 or self.base_x > self.right_side_x or\
		self.base_y < 0 or self.base_y > self.back_side_y:
			self.hide()
			return False
		self.canvas.coords(
			self.id,
			self.base_x - self.rad,
			self.base_y - self.rad,
			self.base_x + self.rad,
			self.base_y + self.rad
		)
		return True

	def hide(self):
		self.canvas.coords(self.id, -10, -10, -10,-10)

class Panzer():
	def __init__(self, canvas, base_x, base_y, length, width, height):
		self.canvas = canvas
		self.base_x = base_x
		self.base_y = base_y
		self.length = length
		self.right_side_x = width
		self.back_side_y = height
		self.rect_id = canvas.create_rectangle(0,0,0,0,
			width = 5, fill = 'red')
		self.gun_id = canvas.create_line(0,0,0,0,
			width = 3, fill = 'black')
		self.gun_dx = 0
		self.gun_dy = -self.length
		self.bullets = []
		self.show_panzer()

	def show_panzer(self):
		self.canvas.coords(
			self.rect_id,
			self.base_x, 
			self.base_y,
			self.base_x + self.length,
			self.base_y + self.length
		)
		self.canvas.coords(
			self.gun_id,
			self.base_x + self.length / 2,
			self.base_y + self.length / 2,
			self.base_x + self.length / 2 + self.gun_dx,
			self.base_y + self.length / 2 + self.gun_dy,
		)
	def move(self, event):
		if event.char == 'a':
			self.base_x = self.base_x - self.length
			if self.base_x < 0:
				self.base_x = self.right_side_x - self.length
		elif event.char == 'd':
			self.base_x = self.base_x + self.length
			if self.base_x > self.right_side_x:
				self.base_x = 0
		elif event.char == 'w':
			self.base_y = self.base_y - self.length
			if self.base_y < 0:
				self.base_y = self.back_side_y - self.length
		elif event.char == 's':
			self.base_y = self.base_y + self.length
			if self.base_y > self.back_side_y:
				self.base_y = 0
		self.show_panzer()

	def fire(self, event):
		self.bullets.append(BallBullet(
			self.base_x + self.length / 2 + self.gun_dx,
			self.base_y + self.length / 2 + self.gun_dy,
			self.gun_dx / self.length,
			self.gun_dy / self.length,
			self.right_side_x,
			self.back_side_y,
			self.canvas
		))

	def move_bullets(self, root):
		#if len(self.bullets) == 0:
			#return
			#print("BYE BYE")
		i = 0
		while i < len(self.bullets):
			if self.bullets[i].move():
				i += 1
				#print("MOV")
			else:
				del self.bullets[i]
				#print("DEL")
		root.after(10, lambda: self.move_bullets(root))

	def targetting(self, event):
		#my_panzer.move_bullets()
		gun_base_x = self.base_x + self.length / 2
		gun_base_y = self.base_y + self.length / 2
		if event.x - gun_base_x != 0:
			angle = math.atan((event.y - gun_base_y) / (event.x - gun_base_x))
		else:
			if event.y < gun_base_y:
				angle = math.pi / 2
			else:
				angle = -math.pi / 2
		if event.x < gun_base_x and event.y < gun_base_y or\
		event.x < gun_base_x and event.y > gun_base_y:
			angle += math.pi
		self.gun_dx = math.cos(angle) * self.length
		self.gun_dy = math.sin(angle) * self.length
		self.canvas.coords(
			self.gun_id,
			gun_base_x,
			gun_base_y,
			gun_base_x + self.gun_dx,
			gun_base_y + self.gun_dy
		)

#def start_game(canvas, width, height):

width = 800
height = 600
panzer_length = 30

root = tk.Tk()
root.geometry(str(width) + "x" + str(height))
canvas = tk.Canvas(root, bg = 'white')
canvas.pack(fill = tk.BOTH, expand = 1)

#start_game(canvas, width, height)
my_panzer = Panzer(canvas, width / 2, height - panzer_length*2, panzer_length, width, height)
root.bind('a', my_panzer.move)
root.bind('d', my_panzer.move)
root.bind('w', my_panzer.move)
root.bind('s', my_panzer.move)
canvas.bind('<Motion>', my_panzer.targetting)
canvas.bind('<Button-1>', my_panzer.fire)


my_panzer.move_bullets(root)

root.mainloop()
