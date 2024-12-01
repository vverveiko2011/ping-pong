from pygame import *
import time as tt
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

    def collidepoint(self, x, y):
        return self.Rect.collidepoint(x, y)

class Player(GameSprite):
    def __init__(self, MImage, MX, MY, MSpeed, MWigth, MHeight):
        super().__init__(MImage, MX, MY, MSpeed, MWigth, MHeight)
        self.Up = False
        self.Down = False


    def update1(self):
        if self.Up and self.Rect.y >= 20:
            self.Rect.y -= self.Speed
            Racket3.Rect.y -= self.Speed
        elif self.Down and self.Rect.y <= 450:
            self.Rect.y += self.Speed
            Racket3.Rect.y += self.Speed
    
    def update2(self):
        if self.Up and self.Rect.y >= 20:
            self.Rect.y -= self.Speed
            Racket4.Rect.y -= self.Speed
        elif self.Down and self.Rect.y <= 450:
            self.Rect.y += self.Speed
            Racket4.Rect.y += self.Speed

class Enemy(GameSprite):

    def __init__(self, MImage, MX, MY, MSpeed, MWigth, MHeight):
        super().__init__(MImage, MX, MY, MSpeed, MWigth, MHeight)
        self.DirectionX = 1
        self.DirectionY = 1


    def update(self):
        global count1
        global count2
        global timeUpdate
        global timeUpdate2
        self.Rect.x += self.Speed*self.DirectionX
        self.Rect.y += self.Speed*self.DirectionY
        if self.Rect.y < 0 or self.Rect.y > 450:
            self.DirectionY *= -1
        if self.colliderect(Racket1.Rect):
            self.DirectionX *= -1
            self.Rect.x += 15
        elif self.colliderect(Racket2.Rect):
            self.DirectionX *= -1
            self.Rect.x -= 15
        else:
            if self.Rect.x < 0:
                count1 += 1
                self.Rect.x = 225
                self.Rect.y = 100
                timeUpdate2 = tt.time()
            elif self.Rect.x > 850:
                count2 += 1
                self.Rect.x = 225
                self.Rect.y = 100
                timeUpdate2 = tt.time()
        

win = display.set_mode((700, 500))
display.set_caption('Ping-Pong')

Background = transform.scale(image.load("background.png"), (700, 500))

Racket1 = Player("racket1.png", 10, 20, 5, 25, 75)
Racket2 = Player("racket2.png", 655, 350, 5, 25, 75)
Racket3 = Player("racket22.png", 16, 94, 5, 15, 40)
Racket4 = Player("racket11.png", 660, 424, 5, 15, 40)

Ball = Enemy("ball.png", 350, 100, 1, 50, 50)

count1 = 0
count2 = 0
timeStart = tt.time()
timeFinish = 0

font1 = font.Font('Comfortaa.ttf', 30)
scoreText = font1.render(str(count1)+" : "+str(count2), True, (0, 0, 0))
timeText = font1.render(str(int(tt.time()-timeStart)), True, (0, 0, 0))
restartText = font1.render("Press 'r' to restart", True, (0, 0, 0))

font2 = font.Font('Comfortaa.ttf', 45)
totalScoreText = font2.render("Score: "+str(count1)+" : "+str(count2), True, (0, 0, 0))
totalTimeText = font2.render(str(timeFinish-timeStart), True, (0, 0, 0))

finish = False
Game = True
FPS = 60
clock = time.Clock()
timeStart = tt.time()
timeUpdate2 = tt.time()
timeUpdate = tt.time()
while Game:

    win.blit(Background, (0, 0))

    if finish != True:
        Racket1.update1()
        Racket2.update2()
        Ball.update()

        Racket1.reset()
        Racket2.reset()
        Racket3.reset()
        Racket4.reset()
        Ball.reset()

        scoreText = font1.render(str(count1)+" : "+str(count2), True, (0, 0, 0))
        timeText = font1.render(str(int(tt.time()-timeStart)), True, (0, 0, 0))
        win.blit(scoreText, (275, 15))
        win.blit(timeText, (385, 15))

        if tt.time()-timeStart > 30:
            timeFinish = tt.time()
            finish = True
        elif count1 == 5 or count2 == 5:
            timeFinish = tt.time()
            finish = True

        if tt.time()-timeUpdate > 0.25:
            timeUpdate = tt.time()
            Ball.Speed = int(tt.time()-timeUpdate2)+2/6
            if Ball.Speed > 3:
                Ball.Speed = 3
            elif Ball.Speed < 1:
                Ball.Speed = 1

        for e in event.get():
            if e.type == QUIT:
                Game = False 
            if e.type == KEYDOWN:
                if e.key == K_UP:
                    Racket2.Up = True
                if e.key == K_DOWN:
                    Racket2.Down = True

                if e.key == K_w:
                    Racket1.Up = True
                if e.key == K_s:
                    Racket1.Down = True

            elif e.type == KEYUP:
                if e.key == K_UP:
                    Racket2.Up = False
                if e.key == K_DOWN:
                    Racket2.Down = False

                if e.key == K_w:
                    Racket1.Up = False
                if e.key == K_s:
                    Racket1.Down = False
    else:
        totalScoreText = font2.render("Score: "+str(count1)+" : "+str(count2), True, (0, 0, 0))
        totalTimeText = font2.render("Time: "+str(int(timeFinish-timeStart)), True, (0, 0, 0))
        win.blit(totalScoreText, (225, 125))
        win.blit(totalTimeText, (250, 170))
        win.blit(restartText, (200, 220))


        for e in event.get():
            if e.type == QUIT:
                Game = False 

            if e.type == KEYDOWN:
                if e.key == K_r:
                    finish = False
                    count1 = 0
                    count2 = 0
                    timeStart = tt.time()
                    timeUpdate2 = tt.time()
                    timeUpdate = tt.time()


    clock.tick(FPS)
    display.update()