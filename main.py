import pygame
import random

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Avoid the Obstacles")

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Load the player image
player = pygame.image.load("character.png")
player = pygame.transform.scale(player, (50, 50))  # Resize if needed
player_x = WIDTH // 2
player_y = HEIGHT - 100
player_speed = 5

# Define obstacle properties
obstacle_width = 50
obstacle_height = 50
obstacle_color = RED
obstacle_list = []
obstacle_speed = 3

# Function to create random obstacles
def create_obstacle():
    x_pos = random.randint(0, WIDTH - obstacle_width)
    y_pos = random.randint(-100, -40)
    return [x_pos, y_pos]

# Add initial obstacles
for _ in range(5):
    obstacle_list.append(create_obstacle())

# Game Loop
running = True
while running:
    screen.fill(WHITE)
    
    # Check for events (like quitting)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the list of keys currently pressed
    keys = pygame.key.get_pressed()

    # Update player position based on keys pressed
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - 50:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < HEIGHT - 50:
        player_y += player_speed

    # Draw the player on the screen
    screen.blit(player, (player_x, player_y))

    # Update obstacle positions
    for obstacle in obstacle_list:
        obstacle[1] += obstacle_speed
        if obstacle[1] > HEIGHT:
            obstacle[1] = random.randint(-100, -40)
            obstacle[0] = random.randint(0, WIDTH - obstacle_width)

        # Draw obstacles
        pygame.draw.rect(screen, obstacle_color, (obstacle[0], obstacle[1], obstacle_width, obstacle_height))

        # Check for collisions with obstacles
        if player_x < obstacle[0] + obstacle_width and player_x + 50 > obstacle[0]:
            if player_y < obstacle[1] + obstacle_height and player_y + 50 > obstacle[1]:
                print("Game Over")
                running = False

    # Update the display
    pygame.display.update()

    # Cap the frame rate
    pygame.time.Clock().tick(30)

pygame.quit()
