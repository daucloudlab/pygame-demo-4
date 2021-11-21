import pygame

W, H = 600, 400
pygame.init()

display_surface = pygame.display.set_mode((W,H))
pygame.display.set_caption("Mouse movement")

display_surface.fill((255,255,255))
pygame.display.flip()
str_drawing = False
sp = ep = None
rect = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            str_drawing = True
            sp = event.pos
        elif event.type == pygame.MOUSEMOTION:
            if str_drawing:
                ep = event.pos
                width = abs(sp[0] - ep[0])
                height = abs(sp[1] - ep[1])
                display_surface.fill((255,255,255))
                rect = pygame.Rect(sp[0], sp[1], width, height)            
                pygame.draw.rect(display_surface, (255,0,0), rect, 3)
                pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            str_drawing = False
            
pygame.quit()