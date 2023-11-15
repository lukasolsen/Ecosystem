from utils.State import EntityState
import random
from manager.Food import Food


class Elf:
    def __init__(self, x, y, color, config):
        self.x = x
        self.y = y
        self.color = color
        self.config = config
        self.speed = random.uniform(config.min_speed, config.max_speed)
        self.angle = 0
        self.state = random.choice(config.behaviors)
        self.rest_time = 0  # Counter for resting time
        self.alert_time = 0  # Counter for alertness time

        self.race = "Elf"
        self.gender = random.choice(["Male", "Female"])

    def move(self, dt, other_entities):
        # Update the position based on different movement behaviors
        state_method = getattr(self, self.state.name.lower())
        if state_method:
            state_method(dt, other_entities)

    def wandering(self, dt, other_entities):
        # Wander around randomly
        self.x += random.uniform(-1, 1) * self.speed * dt
        self.y += random.uniform(-1, 1) * self.speed * dt

        # Find either food or another of the same species
        for other_entity in other_entities:
            if other_entity is not self:
                # For simplicity, let's consider entities within a certain distance
                distance = ((self.x - other_entity.x) ** 2 +
                            (self.y - other_entity.y) ** 2) ** 0.5
                if distance < 20:
                    if isinstance(other_entity, Food):
                        # Change state to eating if food is detected
                        self.state = EntityState.EATING
                    elif other_entity.race == self.race:
                        # Change state to socializing if another of the same species is detected
                        self.state = EntityState.SOCIALIZING

                        if (self.gender != other_entity.gender):
                            # Change state to mating if another of the same species is detected
                            self.state = EntityState.MATING

    def mating(self, dt, other_entities):
        # Mate with another of the same species
        # Wait for a while before they change state to wandering or socializing or resting or exploring
        self.rest_time += dt
        if self.rest_time > random.uniform(5, 10):
            # Wake up and change state to wandering
            self.state = EntityState.WANDERING
            self.rest_time = 0

    def resting(self, dt, other_entities):
        # Sleep for a while
        self.rest_time += dt
        if self.rest_time > random.uniform(5, 10):
            # Wake up and change state to wandering
            self.state = EntityState.WANDERING
            self.rest_time = 0  # Reset rest time

        # While sleeping, move a tiny bit (crawling)
        self.x += random.uniform(-0.1, 0.1) * self.speed * dt
        self.y += random.uniform(-0.1, 0.1) * self.speed * dt

    def exploring(self, dt, other_entities):
        # Explore new places
        self.x += random.uniform(-0.5, 0.5) * self.speed * dt
        self.y += random.uniform(-0.5, 0.5) * self.speed * dt

        # Simulate chance of finding a new place
        if random.random() < 0.03:
            # Change state to wandering and move to the new place
            self.state = EntityState.WANDERING

    def eating(self, dt, other_entities):
        # Eat and stay in the same location
        pass

    def socializing(self, dt, other_entities):
        # Socialize with others, move around a bit
        self.x += random.uniform(-0.2, 0.2) * self.speed * dt
        self.y += random.uniform(-0.2, 0.2) * self.speed * dt

    def alert(self, dt, other_entities):
        # Be alert to potential threats
        self.alert_time += dt
        if self.alert_time > random.uniform(2, 5):
            # Return to normal state after being alert for a while
            self.state = random.choice(
                [EntityState.WANDERING, EntityState.EXPLORING, EntityState.RESTING])
            self.alert_time = 0  # Reset alertness time

        # Move around while being alert
        self.x += random.uniform(-0.3, 0.3) * self.speed * dt
        self.y += random.uniform(-0.3, 0.3) * self.speed * dt

        # Simulate chance of fleeing if a threat is detected
        if random.random() < 0.1:
            self.state = EntityState.FLEEING

    def fleeing(self, dt, other_entities):
        # Flee from a perceived threat
        self.x += random.uniform(-1, 1) * self.speed * dt
        self.y += random.uniform(-1, 1) * self.speed * dt

    # Add more states and behaviors as needed
