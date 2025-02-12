import pygame
from player import Player
from asteroid import Asteroid
from asteroid_field import AsteroidField
from shot import Shot
from constants import BLACK, FRAMERATE, SCREEN_WIDTH, SCREEN_HEIGHT


def main():
    # init the game
    pygame.init()
    # create screen and clock
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    # create group containers
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    # subscribe to group
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    # create a player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()
    # create a delta
    dt = 0
    # game loop
    while True:
        # handle quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # handle screen
        screen.fill(BLACK)
        updatable.update(dt)
        for d in drawable:
            d.draw(screen)
        for a in asteroids:
            if a.collision(player):
                print("Game over !")
                pygame.quit()
                return
        pygame.display.flip()
        # handle framerate
        dt = clock.tick(FRAMERATE) / 1000  # limit the framerate to 60 FPS


if __name__ == "__main__":
    main()
