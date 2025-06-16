import pygame 
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):


    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(surface=screen, color="white", center=self.position, radius=self.radius, width=2)


    def update(self, dt):
        self.position += (self.velocity * dt) 
        return


    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        pos = self.position
        angle = random.uniform(20, 50)
        v1 = self.velocity.rotate(angle)
        v2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(x=pos.x, y=pos.y, radius=new_radius)
        asteroid1.velocity = v1 * 1.2
        asteroid2 = Asteroid(x=pos.x, y=pos.y, radius=new_radius)
        asteroid2.velocity = v2 * 1.2

