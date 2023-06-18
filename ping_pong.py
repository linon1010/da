from pygame import *
from random import randint
from time import time as timer
window = display.set_mode((700, 500))
display.set_caption("ping pong")
window.fill((1 , 250 , 250))
font.init()
run=True

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_size):
        super().__init__()
        self.image = transform.scale(image.load(player_image), player_size)
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_L(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 700 - 80:
            self.rect.y += self.speed
    def update_R(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 700 - 80:
            self.rect.y += self.speed


ball = GameSprite('ball.png' , 300 , 250 , 4 , (50, 50))
racket1 = Player('racket.png', 5 , 250, 4 , (50, 150))
racket2 = Player('racket.png', 635 , 250, 4 , (50, 150))
speedx = 3 
speedy = 3
finish = False
font1 =  font.Font(None , 70)
lose1 = font1.render('player1 проиграл', True , (1 , 0 , 0 ))
lose2 = font1.render('player2 проиграл', True , (1 , 0 , 0 ))


while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if finish != True:
        window.fill((1 , 250 , 250))
        ball.reset()
        racket1.reset()
        racket2.reset()
        racket1.update_L()
        racket2.update_R()
        ball.rect.x += speedx
        ball.rect.y += speedy
    if ball.rect.y > 450 or ball.rect.y < 0:
        speedy *= -1
    if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
        speedx *= -1
    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (100, 100))
    if ball.rect.x > 630:
        finish = True
        window.blit(lose2, (100, 100))
    
    display.update()
    time.delay(40)
