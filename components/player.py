import pygame

from utils.constants import (
    BLACK,
    WHITE,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    IMG_DIR
)

from components.bullet import Bullet
from components.superbullet import Superbullet
from os import path

class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pygame.image.load(path.join(IMG_DIR, "alien.png")).convert()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH/ 2
        self.rect.bottom = SCREEN_HEIGHT -10
        self.bullets = pygame.sprite.Group()

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.rect.x += 5
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if key[pygame.K_LEFT]:
            self.rect.x -= 5
        if self.rect.left < 0:
            self.rect.left = 0
        if key[pygame.K_UP]:
            self.rect.top -= 5
        if self.rect.y < 330:
            self.rect.top = 330
        if key[pygame.K_DOWN]:
            self.rect.bottom += 5
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def shoot(self):
        sound_rifle = pygame.mixer.Sound(path.join(IMG_DIR, "rifle.ogg"))
        pygame.mixer.Sound.play(sound_rifle)
        bullet = Bullet(self.rect.centerx, self.rect.top)
        self.game.all_sprites.add(bullet)
        self.bullets.add(bullet)

    def super_shoot(self):
        sound_rifle = pygame.mixer.Sound(path.join(IMG_DIR, "rifle.ogg"))
        pygame.mixer.Sound.play(sound_rifle)
        super_bullet = Superbullet(self.rect.centerx, self.rect.top)
        self.game.all_sprites.add(super_bullet)
        self.bullets.add(super_bullet)

    def show_timer(self):
        font1 = pygame.font.SysFont("arial", 20, True, False)
        seconds = pygame.time.get_ticks() // 1000
        seconds = str(seconds)
        timer = font1.render(seconds, 0, (WHITE))
        self.screen.blit(timer, (50, 5))
        pygame.display.flip()