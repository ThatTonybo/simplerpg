import pyglet

from opensimplex import OpenSimplex

def draw(window, sprites):
    generator = OpenSimplex(seed=0)

    tilemap = {
        'grass': 'grass.png',
        'sand': 'sand.png',
        'water': 'water.png',
    }
    
    batch = pyglet.graphics.Batch()
    x = 0
    y = 0

    while True:
        n = noise(generator=generator, x=x, y=y)
        t = tile(noise=n)

        img = pyglet.resource.image(tilemap[t])
        sprite = pyglet.sprite.Sprite(img, x=x, y=y, batch=batch)

        sprites[len(sprites)] = sprite

        x += 16

        if x >= window.width:
            y += 16
            x = 0
        if y >= window.height:
            break
    
    return batch

def noise(generator, x, y):
    raw = generator.noise2d(x, y)
    noise = round(raw * 10)

    return noise

def tile(noise):
    if noise <= -3:
        return 'water'
    else:
        if noise <= -1:
            return 'sand'
        elif noise >= 0:
            return 'grass'
        else:
            return None