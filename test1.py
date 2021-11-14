import pygame

DISPLAY_WIDTH = 500
DISPLAY_HEIGHT = 400

pygame.init()
display_surface = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Hello!")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

display_surface.fill(BLUE)

running = True
while running:
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()

pygame.quit()