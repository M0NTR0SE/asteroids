import pygame
import random
from circleshape import CircleShape
from constants import POWERUP_RADIUS, LINE_WIDTH, SCREEN_WIDTH, SCREEN_HEIGHT

class MegaMode(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, POWERUP_RADIUS)

    def draw(self, screen):
        # draw reactangle

        pygame.draw.rect(screen, "red", (self.position.x, self.position.y, POWERUP_RADIUS, POWERUP_RADIUS), LINE_WIDTH)
        # print("megamode has been drawn")

    def update(self, dt):
        pass

class ShotgunMode(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, POWERUP_RADIUS)

    def draw(self, screen):
        # draw reactangle

        pygame.draw.rect(screen, "green", (self.position.x, self.position.y, POWERUP_RADIUS, POWERUP_RADIUS), LINE_WIDTH)
        # print("megamode has been drawn")

    def update(self, dt):
        pass