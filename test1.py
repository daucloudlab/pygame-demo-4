import pygame

DISPLAY_WIDTH = 500
DISPLAY_HEIGHT = 400

pygame.init()
display_surface = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Hello!")

running = True
while running:
    
    for event in pygame.event.get():
        print(event)

        if event.type == pygame.QUIT:
            running = False

pygame.quit()