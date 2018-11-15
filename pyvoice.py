import pygame,sys

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode([640,480])
pygame.time.delay(1000)
pygame.mixer.music.load("Sound/cry.wav")
pygame.mixer.music.set_volume(0.8)
pygame.mixer.music.play(100)

running = True
while running:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running = False

pygame.quit()