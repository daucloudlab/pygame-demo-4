import pygame

W,H = 600,400

pygame.init()

display_surface = pygame.display.set_mode((W, H))
pygame.display.set_caption("Continues keyboard moves")

FPS = 60
clock = pygame.time.Clock()

velocity = 5
x = 100
move = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and event.mod == pygame.KMOD_LCTRL:
                move = -velocity
            elif event.key == pygame.K_RIGHT and event.mod == pygame.KMOD_LCTRL:
                move = velocity
        elif event.type == pygame.KEYUP: 
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                move = 0

    x += move
    print(x)

    display_surface.fill((0,0,0))
    pygame.draw.rect(display_surface, (0,0,255), (x, 100, 20, 20))
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()