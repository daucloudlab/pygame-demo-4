import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300

GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
BLACK = (0, 0, 0)

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Blitting texts")

fonts = pygame.font.get_fonts()
for font in fonts:
    print(font)

system_font = pygame.font.SysFont('Calibri', 64)
system_font_surface = system_font.render("Dragon rules!", True, GREEN, DARKGREEN)
system_font_rect = system_font_surface.get_rect()
system_font_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

custom_font = pygame.font.Font("AttackGraffiti.ttf", 32)
custom_font_surface = custom_font.render("Move the Dragon Soon", True, GREEN)
custom_font_rect = custom_font_surface.get_rect()
custom_font_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2+100)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.blit(system_font_surface, system_font_rect)
    display_surface.blit(custom_font_surface, custom_font_rect)

    pygame.display.update()


pygame.quit()