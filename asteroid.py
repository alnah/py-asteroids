import random
import pygame
from circleshape import CircleShape
from constants import WHITE, THICKNESS, ASTEROID_MIN_RADIUS, ASTEROID_SPEED_UP


class Asteroid(CircleShape):
    def __init__(self, x, y, radius) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, WHITE, self.position, self.radius, THICKNESS)

    def update(self, dt: int) -> None:
        self.position += self.velocity * dt
    
    def split(self) -> None:
        # destroy asteroid
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        # create new random angle and new radius
        random_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        # create new asteroids
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        vector1 = self.velocity.rotate(random_angle)
        vector2 = self.velocity.rotate(-random_angle)
        asteroid1.velocity = vector1 * ASTEROID_SPEED_UP
        asteroid2.velocity = vector2 * ASTEROID_SPEED_UP
