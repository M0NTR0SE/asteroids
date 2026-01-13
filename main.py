import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # initialize game
    pygame.init()

    # set screen size
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # start clock
    clock = pygame.time.Clock()
    dt = 0

    # instantiate groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # add classes to groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # instantiate asteroid field
    asteroid_field = AsteroidField()

    # instantiate player
    x_center = SCREEN_WIDTH / 2
    y_center = SCREEN_HEIGHT / 2
    player = Player(x_center, y_center)

    # start game loop
    while True:
        # log game state
        log_state()

        # monitor for user closing window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # fill screen black
        screen.fill("black")

        # update elements
        updatable.update(dt)

        # check for collisions with the player
        for a in asteroids:
            if a.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        # check for collisions between asteroids and shots
        for a in asteroids:
            for s in shots:
                if s.collides_with(a):
                    log_event("asteroid_shot")
                    a.kill()
                    s.kill()

        # draw elements
        for d in drawable:
            d.draw(screen)

        # refresh screen
        pygame.display.flip()

        # tick clock 60 FPS
        clock.tick(60) # returns the time in ms that has passed since last game loop 
        # dt_temp = clock.tick(60)
        dt = clock.tick(60) / 1000
        # print(f"{dt_temp}, {dt}")

if __name__ == "__main__":
    main()
