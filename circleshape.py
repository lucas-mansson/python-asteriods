import pygame 

class CircleShape(pygame.sprite.Sprite):

    containers = ()

    def __init__(self, x, y, radius):

        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.x = x
        self.y = y
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        #subclasses must override
        pass

    def update(self, dt):
        #subclasses must override
        pass

    def collision(self, other) -> bool:
        distance = self.position.distance_to(other.position)
        return distance <= (self.radius + other.radius)

