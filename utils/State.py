from enum import Enum


class EntityState(Enum):
    WANDERING = "Wandering"       # Roaming without a specific goal
    EATING = "Eating"             # Consuming food
    RESTING = "Resting"           # Taking a break or sleeping
    HUNTING = "Hunting"           # Actively seeking and pursuing prey
    MATING = "Mating"             # Engaging in reproductive activities
    EXPLORING = "Exploring"       # Investigating new surroundings
    ALERT = "Alert"               # Vigilant and aware of surroundings
    FLEEING = "Fleeing"           # Escaping from a perceived threat
    PLAYING = "Playing"           # Engaging in recreational activities
    SOCIALIZING = "Socializing"   # Interacting with others of the same species
