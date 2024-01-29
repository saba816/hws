import pygame
import random
import math
import time

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1800
SCREEN_HEIGHT = 600
PLAYER_SIZE = 30
ENEMY_SIZE_YELLOW = 40
ENEMY_SIZE_GREEN = 25
ITEM_SIZE = 15
WALL_SIZE = 30
PLAYER_SPEED = 5
ENEMY_SPEED_YELLOW = 2
ENEMY_SPEED_GREEN = 3
OBSTACLE_COUNT = 0  # Set the obstacle count to 0

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Advanced 2D Game')

# Load player, enemy, item, and obstacle images
player_image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE), pygame.SRCALPHA)
pygame.draw.rect(player_image, WHITE, (0, 0, PLAYER_SIZE, PLAYER_SIZE))

enemy_yellow_image = pygame.Surface((ENEMY_SIZE_YELLOW, ENEMY_SIZE_YELLOW), pygame.SRCALPHA)
pygame.draw.circle(enemy_yellow_image, YELLOW, (ENEMY_SIZE_YELLOW // 2, ENEMY_SIZE_YELLOW // 2), ENEMY_SIZE_YELLOW // 2)

enemy_green_image = pygame.Surface((ENEMY_SIZE_GREEN, ENEMY_SIZE_GREEN), pygame.SRCALPHA)
pygame.draw.circle(enemy_green_image, GREEN, (ENEMY_SIZE_GREEN // 2, ENEMY_SIZE_GREEN // 2), ENEMY_SIZE_GREEN // 2)

item_image = pygame.Surface((ITEM_SIZE, ITEM_SIZE), pygame.SRCALPHA)
pygame.draw.circle(item_image, BLUE, (ITEM_SIZE // 2, ITEM_SIZE // 2), ITEM_SIZE // 2)

# Player class
class Player:
    def __init__(self, x, y):
        self.image = player_image
        self.rect = self.image.get_rect(center=(x, y))
        self.has_sword = False
        self.score = 0

    def move(self, keys):
        dx = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
        dy = keys[pygame.K_DOWN] - keys[pygame.K_UP]
        self.rect.move_ip(PLAYER_SPEED * dx, PLAYER_SPEED * dy)
        # Wrap around screen
        self.rect.x %= SCREEN_WIDTH
        self.rect.y %= SCREEN_HEIGHT

# Enemy class
class Enemy:
    def __init__(self, x, y, color, size, speed):
        self.color = color
        self.size = size
        self.speed = speed
        self.image = enemy_yellow_image if color == YELLOW else enemy_green_image
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect(center=(x, y))

    def move_towards_player(self, player_rect):
        dx = player_rect.centerx - self.rect.centerx
        dy = player_rect.centery - self.rect.centery
        angle = math.atan2(dy, dx)
        self.rect.move_ip(self.speed * math.cos(angle), self.speed * math.sin(angle))
        # Wrap around screen
        self.rect.x %= SCREEN_WIDTH
        self.rect.y %= SCREEN_HEIGHT

# Item class
class Item:
    def __init__(self, x, y):
        self.image = item_image
        self.rect = self.image.get_rect(center=(x, y))

# Create player
player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# Create enemies
enemies_yellow = [
    Enemy(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT), YELLOW, ENEMY_SIZE_YELLOW, ENEMY_SPEED_YELLOW)
    for _ in range(3)
]

enemies_green = [Enemy(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT), GREEN, ENEMY_SIZE_GREEN, ENEMY_SPEED_GREEN)
    for _ in range(3)]

# Create items
items = [Item(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)) for _ in range(3)]

# Timer variables
start_time = time.time()
spawn_green_timer = 0
spawn_yellow_timer = 0

# Main game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    player.move(keys)

    # Move enemies towards the player
    for enemy in enemies_yellow + enemies_green:
        enemy.move_towards_player(player.rect)

    # Check if the player collects an item
    collected_items = [item for item in items if player.rect.colliderect(item.rect)]
    for item in collected_items:
        items.remove(item)
        items.append(Item(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)))
        player.has_sword = True
        player.score += 1

    # Check if the player slays the green enemy
    if player.has_sword:
        slain_enemies = [enemy for enemy in enemies_green if player.rect.colliderect(enemy.rect)]
        for enemy in slain_enemies:
            enemies_green.remove(enemy)
            player.score += 5

    # Check if the player is caught by a yellow enemy
    caught_by_yellow_enemies = [enemy for enemy in enemies_yellow if player.rect.colliderect(enemy.rect)]
    if caught_by_yellow_enemies:
        print(f"Game Over! Score: {player.score} Time: {int(time.time() - start_time)} seconds")
        pygame.quit()
        exit()

    # Check if the player is caught by a yellow enemy
    caught_by_green_enemies = [enemy for enemy in enemies_green if player.rect.colliderect(enemy.rect)]
    if caught_by_green_enemies:
        print(f"Game Over! Score: {player.score} Time: {int(time.time() - start_time)} seconds")
        pygame.quit()
        exit()

    # Check if it's time to spawn a new green enemy
    if time.time() - spawn_green_timer > 10:
        enemies_green.append(Enemy(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT),
                                   GREEN, ENEMY_SIZE_GREEN, ENEMY_SPEED_GREEN))
        spawn_green_timer = time.time()

    # Check if it's time to spawn a new yellow enemy
    if time.time() - spawn_yellow_timer > 15:
        enemies_yellow.append(Enemy(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT),
                                    YELLOW, ENEMY_SIZE_YELLOW, ENEMY_SPEED_YELLOW))
        spawn_yellow_timer = time.time()

    # Draw background
    screen.fill((0, 0, 0))

    # Draw items
    for item in items:
        screen.blit(item.image, item.rect.topleft)

    # Draw green enemies
    for enemy in enemies_green:
        screen.blit(enemy.image, enemy.rect.topleft)

    # Draw yellow enemies
    for enemy in enemies_yellow:
        screen.blit(enemy.image, enemy.rect.topleft)

    # Draw player
    screen.blit(player.image, player.rect.topleft)

    # Draw score and timer
    font = pygame.font.Font(None, 36)
    score_text = font.render(f'Score: {player.score}', True, WHITE)
    screen.blit(score_text, (10, 10))

    timer_text = font.render(f'Time: {int(time.time() - start_time)} seconds', True, WHITE)
    screen.blit(timer_text, (10, 40))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)







