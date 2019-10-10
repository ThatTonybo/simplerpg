import pyglet

def draw(window, sprites):
    grass = pyglet.resource.image('grass.png')
    
    batch = pyglet.graphics.Batch()
    x = 0
    y = 0

    while True:
        sprite = pyglet.sprite.Sprite(grass, x=x, y=y, batch=batch)

        sprites[len(sprites)] = sprite

        x += grass.width

        if x >= window.width:
            y += grass.height
            x = 0
        if y >= window.height:
            break
    
    return batch