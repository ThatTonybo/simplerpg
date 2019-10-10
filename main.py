import pyglet
from pyglet.window import key

from functions import world, player, update

window = pyglet.window.Window()

pyglet.resource.path = ['resources']
pyglet.resource.reindex()

# pressed down keys
pressed = dict(W=False, A=False, S=False, D=False)

sprites = []

Player = player.Player(pyglet.resource.image('player.png'), x=16, y=16)

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.W:
        pressed['W'] = True
    if symbol == key.A:
        pressed['A'] = True
    if symbol == key.S:
        pressed['S'] = True
    if symbol == key.D:
        pressed['D'] = True

    if symbol == key.ESCAPE:
        window.destroy()
        
@window.event
def on_key_release(symbol, modifiers):
    if symbol == key.W:
        pressed['W'] = False
    if symbol == key.A:
        pressed['A'] = False
    if symbol == key.S:
        pressed['S'] = False
    if symbol == key.D:
        pressed['D'] = False

@window.event
def on_draw():
    window.clear()

    world_batch = world.draw(window, sprites)
    world_batch.draw()

    Player.draw()

print(type(Player))

pyglet.clock.schedule(update.keys(pressed=pressed, player=Player), 1/60)

pyglet.app.run()