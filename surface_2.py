import pygame

W, H = 600, 400
pygame.init()

display_surface = pygame.display.set_mode((W,H))
pygame.display.set_caption("Mouse movement")

display_surface.fill((255,255,255))

sur1 = pygame.Surface((100, 100))
sur1_rect = sur1.get_rect()
sur1.fill((255,0,0))
display_surface.blit(sur1, (50, 100))

sur2 = pygame.Surface((50, 50))
sur2_rect = sur2.get_rect()
sur2.fill((0,255,0))
display_surface.blit(sur2, (200, 100))

sur3_rect = sur1_rect.fit(sur2_rect)
sur1.fill((0,0,255))
display_surface.blit(sur1, sur3_rect)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()

pygame.quit()