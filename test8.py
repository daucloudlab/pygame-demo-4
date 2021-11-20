import pygame

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400

pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Movement restriction")

dragon_image = pygame.image.load('dragon_right.png')
dragon_rect = dragon_image.get_rect()
dragon_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

FPS = 60
clock = pygame.time.Clock()

velocity = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and dragon_rect.left > 0 :
        dragon_rect.x -= velocity
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and dragon_rect.right < WINDOW_WIDTH:
        dragon_rect.x += velocity
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and dragon_rect.top > 0:
        dragon_rect.y -= velocity
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and dragon_rect.bottom < WINDOW_HEIGHT:
        dragon_rect.y += velocity
    
    display_surface.fill((0,0,0))
    display_surface.blit(dragon_image, dragon_rect)

    pygame.display.update()

    clock.tick(FPS)

pygame.quit()