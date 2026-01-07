import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

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

    while True:
        # log game state
        log_state()

        # monitor for user closing window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # fill screen black
        screen.fill("black")

        # refresh screen
        pygame.display.flip()

        # tick clock 60 FPS
        clock.tick(60) # returns the time in ms that has passed since last game loop 
        # dt_temp = clock.tick(60)
        dt = clock.tick(60) / 1000
        # print(f"{dt_temp}, {dt}")

if __name__ == "__main__":
    main()
