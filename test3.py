
import pygame

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300

pygame.init()
# fonts = pygame.font.get_fonts()
# print(fonts)

display_Surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Font test!")

GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)

sysfont = pygame.font.SysFont('Calibri', 64)
sysfont_surface = sysfont.render("Hello PyGame!", GREEN, True, DARKGREEN)
sysfont_rect = sysfont_surface.get_rect()
sysfont_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

customfont = pygame.font.Font('AttackGraffiti.ttf', 36)
customfont_surface = customfont.render("I Love PyGame!", True, GREEN)
customfont_rect = customfont_surface.get_rect()
customfont_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2+100)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_Surface.blit(sysfont_surface, sysfont_rect)
    display_Surface.blit(customfont_surface, customfont_rect)

    pygame.display.update()
    

pygame.quit()