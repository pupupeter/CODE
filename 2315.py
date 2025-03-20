import pygame
import random
import sys
import time

# Initialize pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)  # Correctly defined RED color
BLACK = (0, 0, 0)  # For displaying the score

# Set screen size
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Load background image and resize it to fit the screen
background_image = pygame.image.load("1515.PNG")  # Load background image (use the correct path)
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))  # Resize to screen size

# Load plant and bullet images
plant_image = pygame.image.load("123123.png")  # Load plant image (use the correct path)
plant_image = pygame.transform.scale(plant_image, (50, 50))  # Resize to plant size (50x50)

bullet_image = pygame.image.load("55.jpg")  # Load bullet image (use the correct path)
bullet_image = pygame.transform.scale(bullet_image, (5, 10))  # Resize to bullet size (5x10)

# Load zombie image
zombie_image = pygame.image.load("PVZ2_B_Zombie__76214.jpg")  # Load zombie image (use the correct path)
zombie_image = pygame.transform.scale(zombie_image, (50, 50))  # Resize to zombie size (50x50)

# Plant and Zombie classes
class Plant:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.bullets = []
        self.shoot_timer = 0  # Timer to control bullet firing frequency
        self.speed = 5  # Plant movement speed

    def shoot(self):
        bullet = pygame.Rect(self.x + 20, self.y, 5, 10)  # Bullet from the plant's front
        self.bullets.append(bullet)

    def move_bullets(self):
        for bullet in self.bullets:
            bullet.x += 5  # Bullets move to the right

    def update(self, ticks):  # Update method to control shooting
        self.shoot_timer += ticks
        if self.shoot_timer > 500:  # Fire a bullet every 500ms
            self.shoot()
            self.shoot_timer = 0  # Reset timer

    def move(self, keys):  # Control plant movement
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < SCREEN_WIDTH - 50:
            self.x += self.speed
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y < SCREEN_HEIGHT - 50:
            self.y += self.speed

    def draw(self):
        screen.blit(plant_image, (self.x, self.y))  # Draw the plant using the plant image
        for bullet in self.bullets:
            screen.blit(bullet_image, bullet)  # Draw the bullet using the bullet image

class Zombie:
    def __init__(self):
        self.x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 50)  # Spawn from the right side
        self.y = random.randint(0, SCREEN_HEIGHT)  # Random Y position
        self.speed = random.randint(1, 5)  # Random speed

    def move(self):
        self.x -= self.speed  # Move left

    def draw(self):
        screen.blit(zombie_image, (self.x, self.y))  # Draw the zombie using the zombie image

# Game loop
def game_loop():
    plant = Plant(0, SCREEN_HEIGHT // 2)  # Initial plant position
    zombies = []  # Dynamic zombie generation
    clock = pygame.time.Clock()

    score = 0  # Initial score
    font = pygame.font.Font(None, 36)  # Font for score display

    zombie_spawn_timer = 0  # Timer for spawning zombies
    running = True
    while running:
        ticks = clock.tick(60)  # Limit to 60 FPS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()  # Get keyboard input
        plant.move(keys)  # Update plant's position
        plant.update(ticks)  # Update plant's shooting
        plant.move_bullets()  # Update bullet positions

        # Spawn zombies at intervals
        zombie_spawn_timer += ticks
        if zombie_spawn_timer > 2000:  # Spawn a zombie every 2 seconds
            zombies.append(Zombie())
            zombie_spawn_timer = 0

        # Fill the screen with the background image
        screen.blit(background_image, (0, 0))  # Draw the background image

        # Handle zombie movement and drawing
        plant.draw()

        for zombie in zombies:
            zombie.move()
            zombie.draw()

            # Check for bullet collisions with zombies
            for bullet in plant.bullets:
                if zombie.x < bullet.x < zombie.x + 50 and zombie.y < bullet.y < zombie.y + 50:
                    plant.bullets.remove(bullet)  # Remove the bullet
                    zombies.remove(zombie)  # Remove the zombie
                    zombies.append(Zombie())  # Spawn a new zombie
                    score += 10  # Increase the score

            # Check if a zombie collides with the plant
            if zombie.x < plant.x + 50 and zombie.x + 50 > plant.x and zombie.y < plant.y + 50 and zombie.y + 50 > plant.y:
                running = False  # End the game if collision occurs

        # Remove zombies that have passed off screen
        zombies = [zombie for zombie in zombies if zombie.x > 0]

        # Display score
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))  # Display score in the top left

        pygame.display.flip()  # Update the display
        time.sleep(0.01)  # Control game speed

    # Game over screen
    final_score_text = font.render(f"Game Over! Final Score: {score}", True, BLACK)
    screen.fill(WHITE)
    screen.blit(final_score_text, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))
    pygame.display.flip()
    time.sleep(3)  # Display final score for 3 seconds

    pygame.quit()
    sys.exit()

# Run the game
game_loop()
