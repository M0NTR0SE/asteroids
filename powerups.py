import pygame
import random
from circleshape import CircleShape
from constants import POWERUP_RADIUS

class MegaMode(CirlceShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        