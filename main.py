from pygame import *
font.init()

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
        return self.Rect.colliderect(rect)

class Player(GameSprite):
    def __init__(self, MImage, MX, MY, MSpeed, MWigth, MHeight):
        super().__init__(MImage, MX, MY, MSpeed, MWigth, MHeight)
        self.Up = False
        self.Down = False


    def update(self):
        if self.Up and self.Rect.y >= 20:
            self.Rect.y -= self.Speed
        elif self.Down and self.Rect.y <= 550:
            self.Rect.y += self.Speed

class Enemy(GameSprite):

    def __init__(self, MImage, MX, MY, MSpeed, MWigth, MHeight):
        super().__init__(MImage, MX, MY, MSpeed, MWigth, MHeight)
        self.DirectionX = 1
        self.DirectionY = 1


    def update(self):
        global count1
        global count2
        self.Rect.x += self.Speed*self.DirectionX
        self.Rect.y += self.Speed*self.DirectionY
        if self.Rect.y < 0 or self.Rect.y > 670:
            self.DirectionY *= -1
        elif self.colliderect(Racket1.Rect) or self.colliderect(Racket2.Rect):
            self.DirectionX *= -1
        if self.Rect.x < 0:
            count1 += 1
            self.Rect.x = 225
            self.Rect.y = 100
        elif self.Rect.x > 500:
            count2 += 1
            self.Rect.x = 225
            self.Rect.y = 100
        

win = display.set_mode((500, 700))
display.set_caption('Ping-Pong')

Background = transform.scale(image.load("background.png"), (500, 700))

Racket1 = Player("racket.png", 10, 20, 5, 50, 135)
Racket2 = Player("racket.png", 440, 550, 5, 50, 135)

Ball = Enemy("ball.png", 225, 100, 1, 50, 50)

count1 = 0
count2 = 0

font1 = font.Font('Comfortaa.ttf', 30)
score = font1.render(str(count1)+" : "+str(count2), True, (0, 0, 0))

Game = True
FPS = 60
clock = time.Clock()
while Game:

    win.blit(Background, (0, 0))

    Racket1.update()
    Racket2.update()
    Ball.update()

    Racket1.reset()
    Racket2.reset()
    Ball.reset()

    score = font1.render(str(count1)+" : "+str(count2), True, (0, 0, 0))
    win.blit(score, (150, 25))

    for e in event.get():
        if e.type == QUIT:
            Game = False 

        if e.type == KEYDOWN:
            if e.key == K_UP:
                Racket1.Up = True
            if e.key == K_DOWN:
                Racket1.Down = True

            if e.key == K_w:
                Racket2.Up = True
            if e.key == K_s:
                Racket2.Down = True

        elif e.type == KEYUP:
            if e.key == K_UP:
                Racket1.Up = False
            if e.key == K_DOWN:
                Racket1.Down = False

            if e.key == K_w:
                Racket2.Up = False
            if e.key == K_s:
                Racket2.Down = False

    clock.tick(FPS)
    display.update()