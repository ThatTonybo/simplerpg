import time
from pyglet import *
from pyglet.gl import *
from functions import world, player

key = pyglet.window.key
pyglet.resource.path = ['resources']
pyglet.resource.reindex()

class main(pyglet.window.Window):
	def __init__ (self, width=800, height=600, fps=False, *args, **kwargs):
		super(main, self).__init__(width, height, *args, **kwargs)
		self.x, self.y = 0, 0

		self.keys = {
		}

		self.keymap = 0
		self.keymapTranslation = {
			# bitVal : angle.degrees
			5 : 45,
			1 : 90,
			9 : 135,
			8 : 180,
			10 : 225,
			2 : 270,
			6 : 315,
			4 : 360,
		}

		self.fps_text = '- fps'
		self.fps = 0
		self.last_udpate = time.time()
		self.fps_label = pyglet.text.Label(self.fps_text, x=10, y=self.height - 20)
		
		self.mouse_x = 0
		self.mouse_y = 0

		self.sprites = {}
		self.sprites['player'] = player.Player(pyglet.resource.image('player.png'), x=16, y=16)
		self.world_batch = world.draw(self, self.sprites)

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
		self.fps += 1

		if time.time()-self.last_udpate>1:
			self.fps_label.text = str(self.fps) + ' fps'
			self.fps = 0
			self.last_udpate = time.time()

	def render(self):
		self.clear()

		self.world_batch.draw()
		self.sprites['player'].draw()
		self.fps_label.draw()

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