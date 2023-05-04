from pygame import *

#Создать класс GameSprite(Shooter)
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, speed, width=70, height=70):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
#Cоздать класс Player(Shooter)
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 450:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 450:
            self.rect.y += self.speed

window=display.set_mode((700,500))
window.fill((0,209,209))
clock = time.Clock()
FPS = 30
game =True
finish = True
Racket_r = Player('platform_v.png', 650, 450, 5,15,50)
Racket_l = Player('platform_v.png', 5, 450, 5,15,50)
while game:
    for e in event.get():
        if e.type ==QUIT:
            game = False
    if finish != False:
        window.fill((0,209,209))
        Racket_r.update_r()
        Racket_l.update_l()
        Racket_l.reset()
        Racket_r.reset()
        
    
    display.update()
    clock.tick(30)