import pygame

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300

pygame.init()

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Continous moving test")

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
    if keys[pygame.K_LEFT]:
        dragon_rect.centerx -= velocity
    if keys[pygame.K_RIGHT]:
        dragon_rect.centerx += velocity
    if keys[pygame.K_UP]:
        dragon_rect.centery -= velocity
    if keys[pygame.K_DOWN]:
        dragon_rect.centery += velocity
        
    display_surface.fill((0,0,0))
    display_surface.blit(dragon_image, dragon_rect)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()