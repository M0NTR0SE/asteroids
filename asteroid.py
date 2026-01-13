import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        # kill hit asteroid
        self.kill()

        # check if smallest asteroid
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            # asteroid splits
            log_event("asteroid split")

            # set angle, and radius for new asteroids from split
            split_angle = random.uniform(20, 50)
            posi_angle = self.velocity.rotate(split_angle)
            neg_angle = self.velocity.rotate(-split_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            # create new split asteroids
            new_posi_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            new_neg_asteroid = Asteroid(self.position.x, self.position.y, new_radius)

            # adjust their velocity based on posi_/neg_angle, and increase speed by factor 1.2
            new_posi_asteroid.velocity += posi_angle * 2
            new_neg_asteroid.velocity += neg_angle * 2


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
