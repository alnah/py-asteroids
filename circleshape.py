import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, radius: int) -> None:
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity: pygame.Vector2 = pygame.Vector2(0, 0)
        self.radius: int = radius

    def draw(self, screen: pygame.Surface) -> None:
        # sub-classes must override
        pass

    def update(self, dt: int) -> None:
        # sub-classes must override
        pass

    def collision(self, other: "CircleShape") -> None:
        distance = self.position.distance_to(other.position)
        return distance <= self.radius + other.radius
