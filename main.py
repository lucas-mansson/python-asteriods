import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_MAX_RADIUS, ASTEROID_SPAWN_RATE   
from player import Player


def main():
    print("Starting asteroids")
    pygame.init()

    # Set the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Timer for FPS
    timer = pygame.time.Clock()
    dt = 0

    # Instansiate the player
    player = Player(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
    
    player.draw(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

        time_passed = timer.tick(60)
        dt = time_passed/1000
        

if __name__ == "__main__":
    main()
