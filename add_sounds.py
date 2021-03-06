import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Adding sounds!")

sound_1 = pygame.mixer.Sound('sound_1.wav')
sound_2 = pygame.mixer.Sound('sound_2.wav')

sound_1.play()
pygame.time.delay(2000)
sound_2.play()
pygame.time.delay(2000)
sound_2.set_volume(0.4)
sound_2.play()

pygame.time.delay(5000)
pygame.mixer.music.load('music.wav')
pygame.mixer.music.play(-1, 0.0)
pygame.time.delay(5000)
sound_2.play()
pygame.time.delay(5000)
pygame.mixer.music.stop()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()