import pyglet

def keys(pressed, player):
    if pressed['W'] == True:
        player.up(by=0.5)

    if pressed['A'] == True:
        player.left(by=0.5)

    if pressed['S'] == True:
        player.down(by=0.5)

    if pressed['D'] == True:
        player.right(by=0.5)

