# This is the main file for the Asteroids game
import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Clock = pygame.time.Clock()
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        pygame.display.flip() # Refresh the screen
        dt = Clock.tick(60) / 1000


# This line ensures the main() function is only called when this file is run directly
# and not when it is imported as a module
if __name__ == "__main__":
    main()

