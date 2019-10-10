import pyglet

def keys(pressed, player):
    if pressed['W'] == True:
        player.up(0.5)

    if pressed['A'] == True:
        player.left(0.5)

    if pressed['S'] == True:
        player.down(0.5)

    if pressed['D'] == True:
        player.right(0.5)

