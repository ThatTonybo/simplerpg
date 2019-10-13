import pyglet
from pyglet.gl import *

import time

from math import *

class Player(pyglet.sprite.Sprite):
	def __init__(self, image, x, y, batch=None):
		super(Player, self).__init__(image, x=x, y=y, batch=batch)
		self.last_update = time.time()
		self.target_angle = 0
		self.angle = 0
		self.speed = 0
		self.max_speed = 160
		self.multiplier = 1
		self.turn_speed = 360 # deg/sec
		self.instant_turning = True
		self.x = x
		self.y = y

	def update(self, parent, *args, **kwargs):
		time_last_render = time.time() - self.last_update
		self.last_update = time.time()

		if self.speed == 0:
			return

		speed_factor = time_last_render * (min(self.speed, self.max_speed) * self.multiplier)
		if self.instant_turning:
			turn_factor = self.turn_speed
		else:
			turn_factor = time_last_render * self.turn_speed

		a = self.target_angle - self.angle
		a = (a + 180) % 360 - 180

		a = max(min(a, turn_factor), 0-turn_factor)
		self.angle += (a + 360)
		self.angle %= 360

		x = cos(((self.angle) / 180) * pi)
		y = sin(((self.angle) / 180) * pi)

		self.x += x * speed_factor
		self.y += y * speed_factor

		glTranslatef(-(x * speed_factor), -(y * speed_factor), 0)