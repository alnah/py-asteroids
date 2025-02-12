import pygame

from circleshape import CircleShape
from constants import (
    PLAYER_MOVE_SPEED,
    PLAYER_RADIUS,
    PLAYER_TURN_SPEED,
    SHOT_COUNTDOWN,
    SHOT_SPEED,
    THICKNESS,
    WHITE,
)
from shot import Shot


class Player(CircleShape):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation: int = 0
        self.timer: float = 0

    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, WHITE, self.triangle(), THICKNESS)

    def rotate(self, dt: int) -> None:
        self.rotation += dt * PLAYER_TURN_SPEED

    def move(self, dt: int) -> None:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * dt * PLAYER_MOVE_SPEED

    def shoot(self) -> None:
        if self.timer >= 0:
            return
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * SHOT_SPEED

    def update(self, dt: int) -> None:
        keys = pygame.key.get_pressed()
        self.timer -= dt

        if keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_DOWN]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
            self.timer = SHOT_COUNTDOWN
