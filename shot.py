import pygame

from circleshape import CircleShape
from constants import SHOT_RADIUS, THICKNESS, WHITE


class Shot(CircleShape):
    def __init__(self, x, y) -> None:
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen: pygame.Surface) -> None:
        """Render shot as small white circle for clear visual distinction."""
        pygame.draw.circle(screen, WHITE, self.position, self.radius, THICKNESS)

    def update(self, dt: int) -> None:
        """Update projectile position using inherited velocity-based movement."""
        self.position += self.velocity * dt
