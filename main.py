import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_MAX_RADIUS, ASTEROID_SPAWN_RATE   
from player import Player


def main():
    print("Starting asteroids")
    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    # Set the screen
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Timer for FPS
    timer = pygame.time.Clock()
    dt = 0

    # Instansiate the player
    player = Player(x=SCREEN_WIDTH//2, y=SCREEN_HEIGHT//2)

    #AsteroidField
    field = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt) 

        collided = False
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("game over")
                collided = True
                break
        if collided:
            break        

        # Update the screen
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # FPS
        time_passed = timer.tick(60)
        dt = time_passed/1000
        

if __name__ == "__main__":
    main()
