import pygame


class CircleShape(pygame.sprite.Sprite):
    """Base class initialization for circular game entities."""

    def __init__(self, x: int, y: int, radius: int) -> None:
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity: pygame.Vector2 = pygame.Vector2(0, 0)
        self.radius: int = radius

    def draw(self, screen: pygame.Surface) -> None:
        """Placeholder for renderable entity drawing logic (implemented in subclasses)."""
        pass

    def update(self, dt: int) -> None:
        """Placeholder for frame-based behavior updates (implemented in subclasses)."""
        pass

    def collision(self, other: "CircleShape") -> None:
        """Detect circular collision using distance-based intersection test."""
        distance = self.position.distance_to(other.position)
        return distance <= self.radius + other.radius
