import pygame
from circleshape import CircleShape
from constants import WHITE, THICKNESS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, WHITE, self.position, self.radius, THICKNESS)

    def update(self, dt: int) -> None:
        self.position += self.velocity * dt
