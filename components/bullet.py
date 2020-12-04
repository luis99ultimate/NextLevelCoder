import pygame

from os import path

from utils.constants import (
    RED,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    IMG_DIR,
    BLACK
)
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path.join(IMG_DIR, "bullet.png")).convert()
        self.image = pygame.transform.scale(self.image, (10, 30))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()