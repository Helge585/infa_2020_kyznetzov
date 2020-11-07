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
	pass

class Panzer():
	def __init__(self, canvas, base_x, base_y, length):
		self.canvas = canvas
		self.base_x = base_x
		self.base_y = base_y
		self.length = length
		self.right_side_x = width
		self.rect_id = canvas.create_rectangle(0,0,0,0,
			width = 5, fill = 'red')
		self.gun_id = canvas.create_line(0,0,0,0,
			width = 3, fill = 'black')
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
			self.base_x + self.length / 2,
			self.base_y - self.length,
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
		self.show_panzer()

	def fire(self, event):
		pass

	def targetting(self, event):
		pass

#def start_game(canvas, width, height):
	
width = 800
height = 600
panzer_length = 30

root = tk.Tk()
root.geometry(str(width) + "x" + str(height))
canvas = tk.Canvas(root, bg = 'white')
canvas.pack(fill = tk.BOTH, expand = 1)

#start_game(canvas, width, height)
my_panzer = Panzer(canvas, width / 2, height - panzer_length*2, panzer_length)
root.bind('a', my_panzer.move)
root.bind('d', my_panzer.move)
#scanvas.bind('<Button-1>', my_panzer.move)

tk.mainloop()