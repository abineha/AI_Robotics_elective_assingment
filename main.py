import pygame

pygame.init()

clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)

# Create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Character Control")

# Load background images
bg_images = [pygame.image.load(f"extras/bg_{i}.png").convert() for i in range(1, 11)]
bg_width = bg_images[0].get_width()
bg_height = bg_images[0].get_height()

# Load MP4 audio
pygame.mixer.music.load(r"extras/chill.wav")
pygame.mixer.music.set_volume(0.5)  # Set volume (0.0 to 1.0)
pygame.mixer.music.play(-1)  # Play on loop (-1)

# Load character image
character_image = pygame.image.load("extras\star.png").convert_alpha()
character_width = character_image.get_width()
character_height = character_image.get_height()
character_x = SCREEN_WIDTH // 2  # Initial position at the center of the screen
character_y = SCREEN_HEIGHT // 2

# Define game variables
scroll_x = 0
scroll_speed = 5
character_speed = 5

# Game loop
run = True
while run:
    clock.tick(FPS)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Handle keyboard input for character movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character_x -= character_speed
    if keys[pygame.K_RIGHT]:
        character_x += character_speed
    if keys[pygame.K_UP]:
        character_y -= character_speed
    if keys[pygame.K_DOWN]:
        character_y += character_speed

    # Clear the screen
    screen.fill(WHITE)

    # Draw scrolling background
    for i, bg in enumerate(bg_images):
        bg_rect = bg.get_rect()
        bg_rect.x = i * bg_width + scroll_x
        screen.blit(bg, bg_rect)

    # Update scroll position
    scroll_x -= scroll_speed

    # Draw character
    screen.blit(character_image, (character_x, character_y))

    pygame.display.update()

pygame.quit()
