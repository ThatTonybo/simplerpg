import pyglet

class Player(pyglet.sprite.Sprite):
    def up(self, by):
        self.y += by;

    def down(self, by):
        self.y -= by;

    def left(self, by):
        self.x += by;

    def right(self, by):
        self.x -= by;