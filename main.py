# This is the main file for the Asteroids game
import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2 , SCREEN_HEIGHT / 2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip() # Refresh the screen
        dt = clock.tick(60) / 1000




# This line ensures the main() function is only called when this file is run directly
# and not when it is imported as a module
if __name__ == "__main__":
    main()

