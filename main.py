# This is the main file for the Asteroids game
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import  AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    player = Player(SCREEN_WIDTH / 2 , SCREEN_HEIGHT / 2)
    
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    asteroid_field = AsteroidField()

    Shot.containers = (shots, updatables, drawables)

    dt = 0

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatables.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print ("Game over!")
                sys.exit(0)

            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.kill()

        screen.fill("black")

        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip() # Refresh the screen

        dt = clock.tick(60) / 1000 # Limit framerate to 60


# This line ensures the main() function is only called when this file is run directly
# and not when it is imported as a module
if __name__ == "__main__":
    main()

