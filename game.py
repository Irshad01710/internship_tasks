import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
PLAYER_COLOR, NPC_COLOR = (0, 0, 255), (255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Two Player Racing Game")

player_x, player_y = WIDTH // 3, HEIGHT - 150
npc_x, npc_y = 2 * WIDTH // 3, HEIGHT - 150
player_speed, npc_speed = 5, random.uniform(2, 4)

running = True
while running:
    pygame.time.delay(30)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player_y -= player_speed if keys[pygame.K_UP] else 0
    player_y += player_speed if keys[pygame.K_DOWN] else 0

    npc_y -= npc_speed
    if npc_y < 0:
        npc_y, npc_speed = HEIGHT - 100, random.uniform(2, 4)

    if player_y < 50 or npc_y < 50:
        print("Player wins!" if player_y < 50 else "NPC wins!")
        running = False

    pygame.draw.rect(screen, PLAYER_COLOR, (player_x, player_y, 50, 70))
    pygame.draw.rect(screen, NPC_COLOR, (npc_x, npc_y, 50, 70))
    pygame.display.update()

pygame.quit()
