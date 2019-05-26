import pygame
import time

pygame.init()

hitSound = pygame.mixer.Sound("oof.wav")
fakenews = pygame.mixer.Sound("wrong2.wav")


class player(object):
    ship = pygame.image.load('spaceship.png')
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.vel = 5
        self.walkCount = 0
        self.right = True
        self.left = True

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.left:
            win.blit(self.ship, (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(self.ship, (self.x, self.y))
            self.walkCount += 1
        else:
            if self.right:
                win.blit(self.ship, (self.x, self.y))
            else:
                win.blit(self.ship, (self.x, self.y))
        self.hitbox = (self.x + 2, self.y + 5.5, 29, 52)
        pygame.draw.rect(win, (0,0,0), self.hitbox, 2)






class Projectile(object):
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel = 8



    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)



class amazon(object):
    amazon_pic = pygame.image.load('amazon.png')
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.vel = 3
        self.walkCount = 0

    def draw(self, win):
        self.move()
        if self.walkCount + 1 >= 33:
            self.walkCount = 0
        if self.vel > 0:
            win.blit(self.amazon_pic, (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.amazon_pic, (self.x, self.y))
            self.walkCount += 1
        self.hitbox = (self.x -4, self.y - 2, 75, 70)
        pygame.draw.rect(win, (0, 0, 0), self.hitbox, 2)


    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * - 1
                self.x += self.vel
        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * - 1
                self.x += self.vel

    def hit(self):
        print('hit')
        hitSound.play()

class Trump(object):
    trump_pic = pygame.image.load('trump.jpg')

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.vel = 10
        self.walkCount = 0

    def draw(self, win):
        self.move()
        if self.walkCount + 1 >= 33:
            self.walkCount = 0
        if self.vel > 0:
            win.blit(self.trump_pic, (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.trump_pic, (self.x, self.y))
            self.walkCount += 1
        self.hitbox = (self.x -4, self.y - 2, 75, 70)
        pygame.draw.rect(win, (0, 0, 0), self.hitbox, 2)


    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * - 1
                self.x += self.vel
        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * - 1
                self.x += self.vel

    def hit(self):
        print('hit')
        fakenews.play()

class pikachu(object):
    pikachu = pygame.image.load('pika.gif')

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.vel = 6
        self.walkCount = 0

    def draw(self, win):
        self.move()
        if self.walkCount + 1 >= 33:
            self.walkCount = 0
        if self.vel > 0:
            win.blit(self.pikachu, (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.pikachu, (self.x, self.y))
            self.walkCount += 1
        self.hitbox = (self.x + 12, self.y + 2, 40, 57)
        pygame.draw.rect(win, (0, 0, 0), self.hitbox, 2)

    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * - 1
                self.x += self.vel
        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * - 1
                self.x += self.vel

    def hit(self):
        print('Hit!')
        hitSound.play()







win = pygame.display.set_mode((500,500))

pygame.display.set_caption("Space Invaders")



clock = pygame.time.Clock()




amazon_pic = pygame.image.load('amazon.png')
run = True


player = player(250, 450, 32, 32)
amazon = amazon(1, 250, 64, 64, 450)
pikachu = pikachu(50, 125, 64, 64, 450)
trump = Trump(50, 50, 64, 64, 450)

score_a = 1
score_p = 2
score_t = 10


score = 0
def rwg():
    global walkCount
    win.fill((0,0,0))

    player.draw(win)
    if score_a > 0:
        amazon.draw(win)
    if score_p > 0:
        pikachu.draw(win)
    if score_t > 0:
        trump.draw(win)


    if score_a == 0 and score_p == 0 and score_t == 0:
        win_font = pygame.font.SysFont("arial", 60, True)
        words = win_font.render("You Won!", 1, (255,255,255))
        win.blit(words, (150, 250))

    font = pygame.font.SysFont("arial", 30, True)

    text = font.render("Score: " + str(score), 1, (255,0,0))
    win.blit(text, (300, 10))

    for laser in lasers:
        laser.draw(win)
    pygame.display.update()

lasers = []
shootLoop = 0

t = pygame.time.get_ticks()
c = t
timer = 0
while run:
    c = pygame.time.get_ticks()
    dt = (c - t) / 1000
    t = c

    clock.tick(27)
    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 1:
        shootLoop = 0

    for event in pygame.event.get():
        if event == pygame.QUIT:
            run = False
            break






    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and shootLoop == 0:
        timer += 1
        if timer >= 2:
            timer = 0

            if len(lasers) < 1:
                lasers.append(Projectile(round(player.x + player.w // 2), round(player.y + player.h // 2), 6, (255, 0, 0)))
            shootLoop = 1

    for laser in lasers:
        if score_p > 0:
            if laser.y - laser.radius < pikachu.hitbox[1] + pikachu.hitbox[3] and laser.y + laser.radius > pikachu.hitbox[1]:
                if laser.x + laser.radius > pikachu.hitbox[0] and laser.x - laser.radius < pikachu.hitbox[0] + pikachu.hitbox[2]:
                    pikachu.hit()
                    lasers.pop(lasers.index(laser))
                    score_p -= 1
                    score += 100
        if score_a > 0:
            if laser.y - laser.radius < amazon.hitbox[1] + amazon.hitbox[3] and laser.y + laser.radius > amazon.hitbox[1]:
                if laser.x + laser.radius > amazon.hitbox[0] and laser.x - laser.radius < amazon.hitbox[0] + amazon.hitbox[2]:
                    amazon.hit()
                    lasers.pop(lasers.index(laser))
                    score += 50
                    score_a -= 1
        if score_t > 0:
            if laser.y - laser.radius < trump.hitbox[1] + trump.hitbox[3] and laser.y + laser.radius > trump.hitbox[1]:
                if laser.x + laser.radius > trump.hitbox[0] and laser.x - laser.radius < trump.hitbox[0] + trump.hitbox[2]:
                    trump.hit()
                    lasers.pop(lasers.index(laser))
                    score += 1000
                    score_t -= 1
        if laser.y < 500 and laser.y > 0:
            laser.y -= laser.vel
        else:
            lasers.pop(lasers.index(laser))



    if keys[pygame.K_LEFT] and player.x > player.vel:
        player.x -= player.vel
    elif keys[pygame.K_RIGHT] and player.x < 500 - player.w - player.vel:
        player.x += player.vel
    else:
        walkCount = 0



    rwg()

pygame.quit()

