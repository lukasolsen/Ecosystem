from pyglet import shapes
import pyglet
import random

from manager.Entities.Elf import Elf
from manager.Entity import AnimalConfig


from utils.State import EntityState

from world.Grass import Grass
from world.Sky import Sky
from world.Terrain import Terrain
from world.Tree import Tree


class Ecosystem:
    def __init__(self, num_entities):
        self.entities = []

        # Create a few entities
        self.entities.append(Elf(100, 100, (0, 300, 0), AnimalConfig(
            50, 100, [EntityState.WANDERING, EntityState.EXPLORING, EntityState.RESTING])))
        self.entities.append(Elf(120, 100, (0, 300, 0), AnimalConfig(
            50, 100, [EntityState.WANDERING, EntityState.EXPLORING, EntityState.RESTING])))

        self.terrain = Terrain(800, 600)
        self.grass = Grass(800, 600, density=50)
        self.trees = Tree(800, 600, density=10)
        self.sky = Sky(800, 600)

    def update(self, dt):
        # Update the state of the ecosystem
        for entity in self.entities:
            other_entities = [e for e in self.entities if e is not entity]
            entity.move(dt, other_entities)

    def draw(self, offset_x, offset_y):
        # self.sky.draw()
        self.terrain.draw()
        self.grass.draw(offset_x, offset_y)
        # self.trees.draw(offset_x, offset_y)

        # Draw the entities on the screen with an offset for camera movement
        for entity in self.entities:
            shapes.Circle(entity.x - offset_x, entity.y -
                          offset_y, 10, color=entity.color).draw()
