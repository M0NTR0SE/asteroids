import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_RADIUS, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN_SECONDS, PLAYER_SHOOT_MEGA_MODE 
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_rate_limit = 0
        self.mega_mode = False
        self.shotgun_mode = False
        self.__lives = 3
        self.invincibility_window = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        unit_vector = pygame.Vector2(0,1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        self.shot_rate_limit -= dt
        self.invincibility_window -= dt
    
    def shoot(self):
        if self.shot_rate_limit <= 0:
            shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            shot_velocity = pygame.Vector2(0,1)
            rotated_shot = shot_velocity.rotate(self.rotation)
            rotated_shot_with_speed = rotated_shot * PLAYER_SHOOT_SPEED
            shot.velocity += rotated_shot_with_speed

            if self.shotgun_mode == True:
                self.shotgun(shot_velocity)
            if self.mega_mode == True:
               self.shot_rate_limit = PLAYER_SHOOT_MEGA_MODE 
            else:
                self.shot_rate_limit = PLAYER_SHOOT_COOLDOWN_SECONDS

    def shotgun(self, shot_velocity):
        shot_left = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot_right = Shot(self.position.x, self.position.y, SHOT_RADIUS)

        l_rotated_shot = shot_velocity.rotate(self.rotation - 30)
        r_rotated_shot = shot_velocity.rotate(self.rotation + 30)

        l_rotated_shot_w_speed = l_rotated_shot * PLAYER_SHOOT_SPEED
        r_rotated_shot_w_speed = r_rotated_shot * PLAYER_SHOOT_SPEED 

        shot_left.velocity += l_rotated_shot_w_speed
        shot_right.velocity += r_rotated_shot_w_speed
        

    
    def megamode(self):
        self.mega_mode = True

    def shotgunmode(self):
        self.shotgun_mode = True
        print("shotgunmode activated")

    def get_lives(self):
        return self.__lives
    
    def add_life(self):
        self.__lives += 1
    
    def remove_life(self):
        self.__lives -= 1

    def invincible(self):
        self.invincibility_window = 0.7

    # def mega(self):
    #    if self.shot_rate_limit <= 0:
    #         shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
    #         shot_velocity = pygame.Vector2(0,1)
    #         rotated_shot = shot_velocity.rotate(self.rotation)
    #         rotated_shot_with_speed = rotated_shot * PLAYER_SHOOT_SPEED
    #         shot.velocity += rotated_shot_with_speed
    #         self.shot_rate_limit = PLAYER_SHOOT_MEGA_MODE 

