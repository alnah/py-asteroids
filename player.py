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
        """Calculate vertices for player ship triangle based on current rotation.
        Enables consistent visual representation tied to movement direction."""
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface) -> None:
        """Render player ship as white outlined triangle using calculated vertices."""
        pygame.draw.polygon(screen, WHITE, self.triangle(), THICKNESS)

    def rotate(self, dt: int) -> None:
        """Modify ship orientation based on frame time for smooth rotational movement."""
        self.rotation += dt * PLAYER_TURN_SPEED

    def move(self, dt: int) -> None:
        """Update ship position based on current facing direction."""
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * dt * PLAYER_MOVE_SPEED

    def shoot(self) -> None:
        """Generate new projectile when firing cooldown permits."""
        if self.timer >= 0:
            return
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * SHOT_SPEED

    def update(self, dt: int) -> None:
        """Process player input and update ship state accordingly."""
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
