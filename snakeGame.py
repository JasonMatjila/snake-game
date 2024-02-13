# Importing necessary libraries
import pygame
import sys
import random
import math

# Initializing pygame
pygame.init()
pygame.display.set_caption("Snake Game")

# Constants
SPEED = 10  # Increase the speed value for a faster snake
SNAKE_SIZE = 9
APPLE_SIZE = SNAKE_SIZE
SEPARATION = 10
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
FPS = 25
KEY = {"up": pygame.K_UP, "down": pygame.K_DOWN, "left": pygame.K_LEFT, "right": pygame.K_RIGHT}

# Initializing the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Resources
font = pygame.font.Font(None, 36)
score_font = pygame.font.Font(None, 38)
score_numb_font = pygame.font.Font(None, 28)
game_over_font = pygame.font.Font(None, 48)

# Game clock
clock = pygame.time.Clock()

# Function to check collision between two objects
def check_collision(rect1, rect2):
    return rect1.colliderect(rect2)

# Class for the Apple object
class Apple:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, APPLE_SIZE, APPLE_SIZE)
        self.color = pygame.Color("orange")
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

# Class for the Snake object
class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = KEY["up"]
        self.segments = []
        self.add_segment()
        self.game_over = False
    
    def add_segment(self):
        segment = pygame.Rect(self.x, self.y, SNAKE_SIZE, SNAKE_SIZE)
        self.segments.append(segment)
    
    def move(self):
        if self.direction == KEY["up"]:
            self.y -= SPEED
        elif self.direction == KEY["down"]:
            self.y += SPEED
        elif self.direction == KEY["left"]:
            self.x -= SPEED
        elif self.direction == KEY["right"]:
            self.x += SPEED
        
        # Check if the snake hits the border
        if self.x < 0 or self.x >= SCREEN_WIDTH or self.y < 0 or self.y >= SCREEN_HEIGHT:
            self.game_over = True
        
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].x = self.segments[i - 1].x
            self.segments[i].y = self.segments[i - 1].y
        self.segments[0].x = self.x
        self.segments[0].y = self.y
        
    def grow(self):
        self.add_segment()
    
    def draw(self, screen):
        for segment in self.segments:
            pygame.draw.rect(screen, pygame.Color("green"), segment)

# Function to handle key events
def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key in KEY.values():
                return event.key
    return True

# Main function to run the game
def main():
    snake = Snake(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    apple = Apple(random.randint(0, SCREEN_WIDTH - APPLE_SIZE), random.randint(0, SCREEN_HEIGHT - APPLE_SIZE))
    score = 0
    running = True
    
    while running:
        screen.fill(pygame.Color("black"))
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in KEY.values():
                    snake.direction = event.key
        
        # Snake movement
        snake.move()
        
        # Check if game over
        if snake.game_over:
            running = False
        
        # Collision detection
        if check_collision(snake.segments[0], apple.rect):
            apple.rect.x = random.randint(0, SCREEN_WIDTH - APPLE_SIZE)
            apple.rect.y = random.randint(0, SCREEN_HEIGHT - APPLE_SIZE)
            snake.grow()
            score += 1
        
        # Draw objects
        snake.draw(screen)
        apple.draw(screen)
        
        # Update display
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()

# Start the game
if __name__ == "__main__":
    main()
