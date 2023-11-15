import pyglet
from pyglet import shapes

class Terrain:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self):
        shapes.Rectangle(0, 0, self.width, self.height, color=(34, 139, 34)).draw()
