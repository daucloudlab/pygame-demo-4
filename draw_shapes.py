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
pygame.draw.aaline(display_surface, WHITE, (50, 50), (300, 250))
pygame.draw.lines(display_surface, WHITE, True, [(100, 100), (150, 150), (125, 200)], 5)
pygame.draw.aalines(display_surface, WHITE, True, [(200, 200), (250, 250), (225, 400)])
pygame.draw.polygon(display_surface, WHITE, [(100, 150),(150, 200), (150, 300)])
pygame.draw.rect(display_surface, CYAN, (WINDOW_WIDTH//2, 0, 200, 200))
pygame.draw.circle(display_surface, RED, (WINDOW_WIDTH//2, WINDOW_HEIGHT//2), 100, 4)
pygame.draw.circle(display_surface, YELLOW, (WINDOW_WIDTH//2, WINDOW_HEIGHT//2), 50, 0)
pygame.draw.ellipse(display_surface, WHITE, (200, 400, 250, 150), 1)
pi=3.1415
pygame.draw.arc(display_surface, WHITE, (100, 500, 200, 100), pi/2, 0, 4)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()