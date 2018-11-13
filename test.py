import pygame,random
pygame.init()
screen = pygame.display.set_mode([680,680])
pygame.display.set_caption("游戏")
background = pygame.Surface(screen.get_size())
background.fill((255, 155, 155))
screen.blit(background, (0,0))
my_ball = pygame.image.load("Orb_Icons_001.png")
screen.blit(my_ball,(50,50))
pygame.display.flip()
x = 50
speed = 10


running = True
while running:
    pygame.time.delay(200)
    screen.blit(background, (0, 0))
    x = x + speed
    if x > screen.get_width() - 256 or x < 0:
        speed = -speed
    screen.blit(my_ball, (x, 50))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 接收到退出78事件后退出程序
            pygame.quit()

pygame.quit()