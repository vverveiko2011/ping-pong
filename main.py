from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, MImage, MX, MY, MSpeed, MWigth, MHeight):
        super().__init__()
        self.Image = transform.scale(image.load(MImage), (MWigth, MHeight))
        self.Rect =  self.Image.get_rect()
        self.Rect.x = MX
        self.Rect.y = MY
        self.Speed = MSpeed
    
    def reset(self):
        win.blit(self.Image, (self.Rect.x, self.Rect.y))

    def colliderect(self, rect):
        return self.rect.colliderect(rect)

class Player(GameSprite):
    def __init__(self, MImage, MX, MY, MSpeed, MWigth, MHeight):
        super().__init__(MImage, MX, MY, MSpeed, MWigth, MHeight)

    def move(self):
        if self.Up == True:
            self.Rect.y -= self.Speed

win = display.set_mode((500, 700))
display.set_caption('Ping-Pong')

Background = transform.scale(image.load("background.png"), (500, 700))

Racket1 = Player("racket.png", 10, 10, 5, 350, 400)
Racket2 = Player("racket.png", 490, 10, 5, 350, 400)

Game = True
FPS = 60
clock = time.Clock()
while Game:

    win.blit(Background, (0, 0))

    Racket1.reset()
    Racket2.reset()

    for e in event.get():
        if e.type == QUIT:
            Game = False 

    clock.tick(FPS)
    display.update()