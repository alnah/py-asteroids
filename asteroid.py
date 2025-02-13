import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_SPEED_UP, THICKNESS, WHITE


class Asteroid(CircleShape):
    def __init__(self, x, y, radius) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        """Render asteroid as white outlined circle using pygame drawing primitives."""
        pygame.draw.circle(screen, WHITE, self.position, self.radius, THICKNESS)

    def update(self, dt: int) -> None:
        """Update position using velocity-based movement for consistent physics behavior."""
        self.position += self.velocity * dt

    def split(self) -> None:
        """Handle asteroid destruction and child generation."""
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        vector1 = self.velocity.rotate(random_angle)
        vector2 = self.velocity.rotate(-random_angle)
        asteroid1.velocity = vector1 * ASTEROID_SPEED_UP
        asteroid2.velocity = vector2 * ASTEROID_SPEED_UP
