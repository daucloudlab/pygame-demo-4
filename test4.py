import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Sounds and musics")

sound1 = pygame.mixer.Sound('sound_1.wav')
sound1.play()
pygame.time.delay(2000)
sound2 = pygame.mixer.Sound('sound_2.wav')
sound2.play()
pygame.time.delay(2000)
sound2.set_volume(0.2)
sound2.play()
pygame.time.delay(2000)
pygame.mixer.music.load('music.wav')
pygame.mixer.music.play(-1, 0.0)
sound2.play()
pygame.time.delay(5000*4)
pygame.mixer.music.stop()

running  = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()