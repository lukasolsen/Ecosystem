from enum import Enum

# Need things for Grass, Trees, Main Terrain, Water, Flowing Water, etc.


class TerrainColors(Enum):
    Grass = (0, 255, 0)
    Dirt = (139, 69, 19)
    Water = (0, 0, 255)
    FlowingWater = (0, 0, 255)
    Sand = (255, 255, 0)
    Snow = (255, 255, 255)
    Stone = (128, 128, 128)
    Rock = (128, 128, 128)
    Wood = (139, 69, 19)
    Leaves = (0, 100, 0)
    Flower = (255, 0, 255)
    TallGrass = (0, 255, 0)
    DeadBush = (139, 69, 19)
    Cactus = (0, 255, 0)
    Reeds = (0, 255, 0)
    Mushroom = (255, 0, 0)
    Pumpkin = (255, 0, 0)
