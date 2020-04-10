# Import pygame module
import pygame

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Define a player object by extending pygame.sprite.SPrite
# The sruface dawn on the screen is now an attribute of "player"
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

# Intialize pygame
pygame.init()

# Create the screen object
# The size is determined by constants SCREEN_WIDTH AND SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Instantiate the player. Will be rectangle initially
player = Player()

# Variable to keep the main loop running
running = True

# Main loop
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
            if event.type == KEYDOWN:
                # Was it the ESCAPE key? If so, stop the loop
                if event.key == K_ESCAPE:
                    running = False
            # Did the user click the window close button? If so, stop the loop.
            elif event.type == QUIT:
                running = False

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw the player on the screent
    screen.blit(player.surf, player.rect)

    # Update the display
    pygame.display.flip()