import pygame

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Draw Shapes")

display_surface.fill(BLUE)

pygame.draw.line(display_surface, WHITE, (0, 0), (300, 200), 4)
pygame.draw.circle(display_surface, RED, (WINDOW_WIDTH//2, WINDOW_HEIGHT//2), 100, 4)
pygame.draw.circle(display_surface, YELLOW, (WINDOW_WIDTH//2, WINDOW_HEIGHT//2), 50, 0)
pygame.draw.rect(display_surface, CYAN, (WINDOW_WIDTH//2, 0, 200, 200))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()