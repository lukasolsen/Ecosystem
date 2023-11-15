import pyglet
from pyglet import shapes
import random

class Tree:
    def __init__(self, width, height, density):
        self.width = width
        self.height = height
        self.density = density
        self.tree_positions = self.generate_tree_positions()

    def generate_tree_positions(self):
        tree_positions = []
        for _ in range(self.density):
            x = random.uniform(0, self.width)
            y = random.uniform(0, self.height)
            tree_positions.append((x, y))
        return tree_positions

    def draw(self, offset_x, offset_y):
        for x, y in self.tree_positions:
            shapes.Rectangle(x - offset_x, y - offset_y, 10, 20, color=(139, 69, 19)).draw()
