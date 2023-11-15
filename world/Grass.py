import pyglet
from pyglet import shapes
import random
from utils.Colors import TerrainColors


class Grass:
    def __init__(self, width, height, density):
        self.width = width
        self.height = height
        self.density = density
        self.grass_positions = self.generate_grass_positions()

    def generate_grass_positions(self):
        grass_positions = []
        for _ in range(self.density):
            x = random.uniform(0, self.width)
            y = random.uniform(0, self.height)
            grass_positions.append((x, y))
        return grass_positions

    def draw(self, offset_x, offset_y):
        for x, y in self.grass_positions:
            shapes.Rectangle(x - offset_x, y - offset_y, 3,
                             10, color=TerrainColors.Grass.value).draw()
