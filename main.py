# This is the main file for the Asteroids game
import pygame
from constants import *

def main():
    # Initialize the pygame library
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black") # Fill the screen with black
        pygame.display.flip() # Refresh the screen

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

# This line ensures the main() function is only called when this file is run directly
# and not when it is imported as a module
if __name__ == "__main__":
    main()

