import pygame 

class CircleShape(pygame.sprite.Sprite):

    containers = ()

    def __init__(self, x: int, y: int , radius: int):

        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        #subclasses must override
        pass

    def update(self, dt):
        #subclasses must override
        pass
