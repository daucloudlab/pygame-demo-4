import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Discrete Keyboard movement")

dragon_image = pygame.image.load('dragon_left.png')
dragon_rect = dragon_image.get_rect()
dragon_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

running = True
while running:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dragon_rect.centerx -= 10
            if event.key == pygame.K_RIGHT:
                dragon_rect.centerx += 10

    display_surface.fill((0,0,0))
    display_surface.blit(dragon_image, dragon_rect)
    
    pygame.display.update()

pygame.quit()