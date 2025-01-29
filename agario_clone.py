import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Agar.io Clone")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Clock for controlling the frame rate
clock = pygame.time.Clock()
FPS = 60

# Player class
class Player:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)

    def move(self, mouse_x, mouse_y):
        # Move towards the mouse position
        self.x += (mouse_x - self.x) * 0.05
        self.y += (mouse_y - self.y) * 0.05

# Food class
class Food:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)

# Initialize player and food
player = Player(WIDTH // 2, HEIGHT // 2, 20, BLUE)
foods = [Food(random.randint(0, WIDTH), random.randint(0, HEIGHT), 10, GREEN) for _ in range(20)]

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Move player
    player.move(mouse_x, mouse_y)

    # Check for collisions with food
    for food in foods[:]:
        if (player.x - food.x)**2 + (player.y - food.y)**2 <= (player.size + food.size)**2:
            player.size += 1  # Grow the player
            foods.remove(food)  # Remove the eaten food
            foods.append(Food(random.randint(0, WIDTH), random.randint(0, HEIGHT), 10, GREEN))  # Add new food

    # Draw everything
    screen.fill(WHITE)
    player.draw(screen)
    for food in foods:
        food.draw(screen)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()