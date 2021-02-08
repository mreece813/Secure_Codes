import pygame
from random import randint

####################
pygame.init()

width = 800
height = 600

radius = width//80
dia = radius * 2

white = [255,255,255]
black = [0,0,0]
purple = [255,0,255]
appleColor = [200,45,0]

clock = pygame.time.Clock()

win = pygame.display.set_mode((width,height))


class Apple:

    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, win):
        pygame.draw.circle(win,appleColor, (self.x,self.y), radius)

class Snake:

    
    

    def __init__(self, color,  length = 4):


        self.x = [width//2]
        self.y = [height//2]
        self.gap = 2
        self.interval = self.gap + dia
        self.direction = -1
        self.score = 0
        self.length = length
        self.color = color
        for i in range(1,self.length):
            self.x.append(self.x[-1])
            self.y.append(self.y[-1] + self.interval * i)

    def update(self):

        if len(self.x) < self.length:
            self.x.append(self.x[-1])
            self.y.append(self.y[-1])

        for i in range(self.length -1, 0, -1): #Moves each circle to the location of the circle ahead of it
            self.x[i] = self.x[i-1]            #Retains the snake's trail
            self.y[i] = self.y[i-1]

        if self.direction == 0:
            self.x[0] += self.interval
        if self.direction == 1:
            self.x[0] -= self.interval
        if self.direction == 2:
            self.y[0] -= self.interval
        if self.direction == 3:
            self.y[0] += self.interval

        if self.x[0] > width:
            self.x[0] = radius
        if self.x[0] < 0:
            self.x[0] = width - radius
        if self.y[0] > height:
            self.y[0] = radius
        if self.y[0] < 0:
            self.y[0] = height - radius

            
    def draw(self,win,position):
        for i in range(self.length):
            pygame.draw.circle(win, self.color, (self.x[i], self.y[i]), radius)
        scoreFont = pygame.font.SysFont('Comic Sans', 25)
        scoreDisplay = scoreFont.render('Score: ' + str(self.score), 1, [0,255,0])
        if position == 'topleft':
            win.blit(scoreDisplay, (0,0))
        if position == 'topright':
            win.blit(scoreDisplay, (width-70, 0))

def collisionChecker(x1,y1,rad1,x2,y2,rad2):     ##Determines if two circle collide
    if x1 + rad1/2 >= x2 - rad2 and x1- rad1/2 <= x2 + rad2:
        if y1 +rad1/2 >= y2 - rad2 and y1 -rad1/2 <= y2 + rad2:
            return True
    return False



def redrawGameWindow():
    win.fill(black)
    player1.update()
    player2.update()
    player1.draw(win,'topleft')
    player2.draw(win,'topright')
    apple.draw(win)
    pygame.display.update()

def gameOver(winner,loser):
    winner.score += 5
    gameString = ''
    if player1.score > player2.score:
        gameString += 'Player 1 wins!'
    elif player2.score > player1.score:
        gameString += 'Player 2 wins!'
    else:
        gameString += "It's a draw"
    gameText = gameOverFont.render(gameString, 1, appleColor)
    win.fill(black)
    win.blit(gameText, (width//2 - 200, height//2 -40))
    player1.draw(win,'topleft')
    player2.draw(win,'topright')
    pygame.display.update()
    
    
    
    
#######################################
#          Main Loop




running = True
apple = Apple(randint(10, width -10), randint(10,height -10))
player1 = Snake(white)
player2 = Snake(purple)
gameOverFont = pygame.font.SysFont('Comic Sans', 80)

while running:

    clock.tick(15)
    i = 0
    i += 1
    if i > 4:
        i =0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]: ####Player1 Movement
        player1.direction = 0
    if keys[pygame.K_LEFT]:
        player1.direction = 1
    if keys[pygame.K_UP]:
        player1.direction = 2
    if keys[pygame.K_DOWN]:
        player1.direction = 3

    if keys[pygame.K_a]:
        player2.direction = 1
    if keys[pygame.K_d]:
        player2.direction = 0
    if keys[pygame.K_s]:
        player2.direction = 3
    if keys[pygame.K_w]:
        player2.direction = 2

    if collisionChecker(player1.x[0], player1.y[0], radius, apple.x, apple.y, radius): ####Was an apple eaten
        apple = 0
        apple= Apple(randint(10, width -10), randint(10,height -10))
        player1.length += 1
        player1.score += 1

    if collisionChecker(player2.x[0], player2.y[0], radius, apple.x, apple.y, radius): ####Was an apple eaten
        apple = 0
        apple= Apple(randint(10, width -10), randint(10,height -10))
        player2.length += 1
        player2.score += 1

    for i in range(3,player1.length-1):   ##Did the player1 collide with itself  or the other?
        if collisionChecker(player1.x[0],player1.y[0],0,player1.x[i], player1.y[i], radius):
            gameOver(player2,player1)
            pygame.time.delay(5000)
            player1 = 0
            player1 = Snake(white)
            player2 = 0
            player2 = Snake(purple)
    for i in range(3,player2.length-1):
        if collisionChecker(player1.x[0],player1.y[0],0,player2.x[i], player2.y[i], radius):
            gameOver(player2,player1)
            pygame.time.delay(5000)
            player1 = 0
            player1 = Snake(white)
            player2 = 0
            player2 = Snake(purple)
                

    for i in range(3,player2.length-1):   ##Did the player2 collide with itself or other?
        if collisionChecker(player2.x[0],player2.y[0],0,player2.x[i], player2.y[i], radius):
            gameOver(player1, player2)
            pygame.time.delay(5000)
            player1 = 0
            player1 = Snake(white)
            player2 = 0
            player2 = Snake(purple)
    for i in range(3,player1.length-1):
        if collisionChecker(player2.x[0],player2.y[0],0,player1.x[i], player1.y[i], radius):
            gameOver(player2,player1)
            pygame.time.delay(5000)
            player1 = 0
            player1 = Snake(white)
            player2 = 0
            player2 = Snake(purple)
    redrawGameWindow()

pygame.quit()
    
