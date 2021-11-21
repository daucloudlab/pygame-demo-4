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
    
    pressed = pygame.mouse.get_pressed()
    if pressed[0]:
        ep = pygame.mouse.get_pos()
        if sp is None:
            sp = ep
        width = abs(sp[0]-ep[0])
        height = abs(sp[1]-ep[1])
        display_surface.fill((255,255,255))
        pygame.draw.rect(display_surface, (255,0,0), (sp[0], sp[1], width, height))
        pygame.display.update()
    else:
        sp = None

            
pygame.quit()