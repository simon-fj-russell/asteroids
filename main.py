import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    pygame_clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        player.update(dt)
        screen.fill("black")
        # draw the player
        player.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = pygame_clock.tick(60) / 1000

if __name__ == "__main__":
    main()