import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from powerups import MegaMode

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    # print(f"{pygame.font.get_fonts()}")

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
    MegaMode.containers = (drawable)

    # instantiate player
    x_center = SCREEN_WIDTH / 2
    y_center = SCREEN_HEIGHT / 2
    player = Player(x_center, y_center)

    # instantiate asteroid field
    asteroid_field = AsteroidField()
    
    # instantiate powerups
    # megamode = MegaMode(player.position.x + 100, player.position.y)

    # asteroid killed counter
    asteroid_killed = 0

    # text
    # colours
    white = (255, 255, 255)

    # text generate
    melon_pop_font = pygame.font.Font('melon pop.ttf', 32)
    score = melon_pop_font.render(f"Score: {asteroid_killed}", True, white)
    score_rect = score.get_rect()
    score_rect.center = (1080, 600)

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
                    # kill asteroid that was hit by shot
                    a.split()
                    # track the amount of asteroids killed
                    asteroid_killed += 1
                    print(f"Asteroids killed: {asteroid_killed}")

                    # kill shot that hit asteroid
                    s.kill()

                    if asteroid_killed == 5:
                        megamode = MegaMode(player.position.x + 100, player.position.y)


        # check for powerups
        if asteroid_killed >= 5:
            if player.collides_with(megamode):
                player.power_upped()
                megamode.kill()

        # write text to screen
        score = melon_pop_font.render(f"Score: {asteroid_killed}", True, white)
        screen.blit(score, score_rect)

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
