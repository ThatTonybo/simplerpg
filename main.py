import time
from pyglet import *
from pyglet.gl import *
from functions import world
from math import *

key = pyglet.window.key
pyglet.resource.path = ['resources']
pyglet.resource.reindex()

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
		self.x = x
		self.y = y

	def update(self, parent, *args, **kwargs):
		## == This will update the direction and position
		## * Get the time since last render/update (because
		##   we'll be updating based on time, not frames)
		time_last_render = time.time() - self.last_update
		self.last_update = time.time()

		## If we're standing still, fuck it - abort!
		if self.speed == 0:
			return

		## Calculate the speed based of speed over time
		## Same for turning.
		speed_factor = time_last_render * (min(self.speed, self.max_speed)*self.multiplier)
		turn_factor = time_last_render * self.turn_speed

		## 
		#wself.target_angle = ((atan2(mouse_y-self.y, mouse_x-self.x)/pi*180)+360)%360
		a = self.target_angle - self.angle
		a = (a + 180) % 360 - 180

		a = max(min(a, turn_factor), 0-turn_factor)
		self.angle += (a+360)
		self.angle %= 360

		x = cos(((self.angle)/180)*pi)
		y = sin(((self.angle)/180)*pi)

		self.x += x * speed_factor
		self.y += y * speed_factor

class main(pyglet.window.Window):
	def __init__ (self, width=800, height=600, fps=False, *args, **kwargs):
		super(main, self).__init__(width, height, *args, **kwargs)
		self.x, self.y = 0, 0

		self.keys = {
		}

		self.keymap = 0
		self.keymapTranslation = {
			# bitVal : angle.degrees
			#0 : 0, # <- Turns turning off
			5 : 45,
			1 : 90,
			9 : 135,
			8 : 180,
			10 : 225,
			2 : 270,
			6 : 315,
			4 : 360,
		}
		
		self.mouse_x = 0
		self.mouse_y = 0

		self.sprites = {}
		self.sprites['player'] = Player(pyglet.resource.image('player.png'), x=16, y=16)

		self.alive = 1

	def on_draw(self):
		self.render()

	def on_close(self):
		self.alive = 0

	def on_mouse_motion(self, x, y, dx, dy):
		self.mouse_x = x

	def on_key_release(self, symbol, modifiers):
#		if symbol == key.W:
#			pressed['W'] = False
#		if symbol == key.A:
#			pressed['A'] = False
#		if symbol == key.S:
#			pressed['S'] = False
#		if symbol == key.D:
#			pressed['D'] = False

		del self.keys[symbol]

		if key.W == symbol:
			self.keymap ^= 1
		if key.S == symbol:
			self.keymap ^= 2
		if key.D == symbol:
			self.keymap ^= 4
		if key.A == symbol:
			self.keymap ^= 8

		if self.keymap in self.keymapTranslation:
			self.sprites['player'].target_angle = self.keymapTranslation[self.keymap]
		else:
			self.sprites['player'].speed = 0

	def on_key_press(self, symbol, modifiers):
		if symbol == key.ESCAPE: # [ESC]
			self.alive = 0

		self.keys[symbol] = time.time()

		if key.W in self.keys:
			print('Up')
			self.keymap |= 1
		if key.S in self.keys:
			print('Down')
			self.keymap |= 2
		if key.D in self.keys:
			print('Right')
			self.keymap |= 4
		if key.A in self.keys:
			print('Left')
			self.keymap |= 8

		if self.keymap in self.keymapTranslation:
			self.sprites['player'].target_angle = self.keymapTranslation[self.keymap]

	def update(self):
		if self.keymap in self.keymapTranslation:
			#self.sprites['player'].speed += 1
			self.sprites['player'].speed = 160
		self.sprites['player'].update(self)

	def render(self):
		self.clear()

		world_batch = world.draw(self, self.sprites)
		world_batch.draw()

		self.sprites['player'].draw()

		self.flip()

	def run(self):
		while self.alive == 1:
			self.update()
			self.render()

			# -----------> This is key <----------
			# This is what replaces pyglet.app.run()
			# but is required for the GUI to not freeze
			#
			event = self.dispatch_events()

if __name__ == '__main__':
	x = main()
	x.run()