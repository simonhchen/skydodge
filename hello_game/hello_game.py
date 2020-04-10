# Simply pygame program

# Import and intiialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode((500,500))

# Game loop. Run until the user asks to quite
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255)) # RGB values

    # Draw a solid blue circle in the center
    # first tuple is for color, second tuple is where it is, 75 is radius
    pygame.draw.circle(screen, (0, 0, 255), (250,250), 75)

    # Flip the display
    pygame.display.flip()

# Done! time to quit
pygame.quit