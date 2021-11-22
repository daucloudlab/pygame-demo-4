import pygame

W,H = 600,400

pygame.init()

display_surface = pygame.display.set_mode((W,H))
pygame.display.set_caption("Text demo")

font = pygame.font.SysFont("Calibri", 32)
text = font.render("Text demo app", True, (0, 255, 0), (10, 50, 10))
text_rect = text.get_rect()
text_rect.center = (W//2, H//2)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pygame.mouse.get_rel()

    if pygame.mouse.get_focused() and text_rect.collidepoint(pygame.mouse.get_pos()):
        btns = pygame.mouse.get_pressed()
        if btns[0]:
            rel = pygame.mouse.get_rel()
            text_rect.move_ip(rel)

    display_surface.fill((0,0,0))
    display_surface.blit(text, text_rect)
    pygame.display.update()


pygame.quit()