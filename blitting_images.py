import pygame


DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 300

pygame.init()

display_surface = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("blitting images")

dragon_left_image = pygame.image.load('dragon_left.png')
dragon_left_rect = dragon_left_image.get_rect()
dragon_left_rect.topleft = (0, 0)

dragon_right_image = pygame.image.load('dragon_right.png')
dragon_right_rect = dragon_right_image.get_rect()
dragon_right_rect.topright = (DISPLAY_WIDTH, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # display_surface.fill((0,0,255))
    display_surface.blit(dragon_left_image, dragon_left_rect)
    display_surface.blit(dragon_right_image, dragon_right_rect)
    pygame.draw.line(display_surface, (255, 255, 255), (0, 75), (DISPLAY_WIDTH, 75),4)

    pygame.display.update()

pygame.quit()