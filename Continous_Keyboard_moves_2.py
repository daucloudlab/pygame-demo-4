import pygame

W,H = 600,400

pygame.init()

display_surface = pygame.display.set_mode((W, H))
pygame.display.set_caption("Continues keyboard moves")

FPS = 60
clock = pygame.time.Clock()

velocity = 5
x = 100
is_left, is_right = False, False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                is_left = True
            elif event.key == pygame.K_RIGHT:
                is_right = True
        elif event.type == pygame.KEYUP: 
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                is_right = is_left = False

    if is_left:
        x -= velocity
    elif is_right:
        x += velocity
        
    display_surface.fill((0,0,0))
    pygame.draw.rect(display_surface, (0,0,255), (x, 100, 20, 20))
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()