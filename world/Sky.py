import pyglet
from pyglet import shapes


class Sky:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self):
        shapes.Rectangle(0, 0, self.width, self.height,
                         color=(135, 206, 250)).draw()
