import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH = 800
HEIGHT = 600
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
BALL_SIZE = 20
FPS = 60

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Set up the paddles
paddle1 = pygame.Rect(0, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle2 = pygame.Rect(
    WIDTH - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT
)
score1 = score2 = 0

# Set up the ball
ball = pygame.Rect(0, 0, BALL_SIZE, BALL_SIZE)
ball_speed_x = 5
ball_speed_y = 5

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        paddle1.y -= 5
    if keys[pygame.K_DOWN]:
        paddle1.y += 5
    if keys[pygame.K_w]:
        paddle2.y -= 5
    if keys[pygame.K_s]:
        paddle2.y += 5

    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Check for collisions with the paddles and walls
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed_x = -ball_speed_x
    if ball.y < 0:
        ball_speed_y = -ball_speed_y
    elif ball.y > HEIGHT - BALL_SIZE:
        ball_speed_y = -ball_speed_y

    # Check for scoring
    if ball.x < 0:
        score2 += 1
        ball.x = WIDTH / 2
        ball.y = HEIGHT / 2
        ball_speed_x = 5
        ball_speed_y = 5
    elif ball.x > WIDTH - BALL_SIZE:
        score1 += 1
        ball.x = WIDTH / 2
        ball.y = HEIGHT / 2
        ball_speed_x = -5
        ball_speed_y = 5

    # Draw everything
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), paddle1)
    pygame.draw.rect(screen, (255, 255, 255), paddle2)
    pygame.draw.ellipse(screen, (255, 255, 255), ball)

    # Display the score
    font = pygame.font.Font(None, 36)
    text = font.render(f"{score1} - {score2}", True, (255, 255, 255))
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 20))

    # Update the display
    pygame.display.flip()
    clock.tick(FPS)
