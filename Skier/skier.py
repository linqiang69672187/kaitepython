import pygame,sys,random

skier_images = ["skier_down.png","skier_right1.png","skier_right2.png","skier_left2.png","skier_left1.png"]
class SkierClass(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(skier_images[0])
        self.rect = self.image.get_rect()
        self.rect.center = [320,100]
        self.angle = 0
    def trun(self,direction):
        self.angle = self.angle+direction
        if self.angle <-2:
            self.angle = -2
        if self.angle >2:
            self.angle = 2
        center = self.rect.center
        self.image = pygame.image.load(skier_images[self.angle])
        self.rect = self.image.get_rect()
        self.rect.center = center
        speed = [self.angle,6-abs(self.angle)*2]
        return  speed
    def move(self,speed):
        self.rect.centerx = self.rect.centerx + speed[0]
        if self.rect.centerx < 20:self.rect.centerx = 20
        if self.rect.centerx > 620:self.rect.centerx = 620
class ObstacleClass(pygame.sprite.Sprite):
    def __init__(self,imagefile,location,type):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imagefile)
        self.rect = self.image.get_rect()
        self.rect.center = location
        self.type = type
        self.passed = False

    def update(self):
        global speed
        self.rect.centery -=speed[1]
        if self.rect.centery <-32:
            self.kill()
def create_map():
    global obstacles
    locations = []
    for i in range(10):
        row  = random.randint(0,9)
        col = random.randint(0,9)
        location = [col*64+32,row*64+32+640]
        if not (location in locations):
            locations.append(location)
            type  = random.choice(["tree","flag"])
            if type =="tree":img="skier_tree.png"
            elif type=="flag":img="skier_flag.png"
            obstacle = ObstacleClass(img,location,type)
            obstacles.add(obstacle)

def animate():
    screen.fill([255,255,255])
    obstacles.draw(screen)
    screen.blit(skier.image,skier.rect)
    pygame.display.flip()

pygame.init()
screen  = pygame.display.set_mode([640,640])
clock = pygame.time.Clock()
points = 0
speed = [0,6]
skier = SkierClass()
obstacles = pygame.sprite.Group()
create_map()
map_position = 0
running = True

while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:running=False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed = skier.trun(-1)
            elif event.key == pygame.K_RIGHT:
                speed = skier.trun(1)
    skier.move(speed)

    map_position+=speed[1]

    if map_position >= 640:
        create_map()
        map_position = 0
    obstacles.update()
    animate()

pygame.quit()
