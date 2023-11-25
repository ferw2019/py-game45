import pygame
import sys

pygame.init()
clock = pygame.time.Clock()

WIDTH, HEIGHT = 920,620
PLAYER_SIZE = 55
PLATFORM_SIZE = 105
PLAYER_COLOR = (255, 0, 0)
PLATFORM_COLOR = (0, 255, 0)
BACKGROUND_COLOR = (0, 0, 0)
GRAVITY = 1
JUMP_HEIGHT = 15
screen = pygame.display.set_mode((WIDTH, HEIGHT))

player = pygame.Rect(WIDTH // 2 - PLAYER_SIZE // 2, HEIGHT // 2 - PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE)
player_speed = 5
player_v_speed = 0

platforms = [
    pygame.Rect(WIDTH // 2 - PLAYER_SIZE, 500, PLATFORM_SIZE, 10),
    pygame.Rect(600, 500, PLATFORM_SIZE, 10),
    pygame.Rect(120, 550, PLATFORM_SIZE, 10)
]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(BACKGROUND_COLOR)
    for platform in platforms:
        pygame.draw.rect(screen, PLATFORM_COLOR, platform)
    pygame.draw.rect(screen, PLAYER_COLOR, player)
    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)