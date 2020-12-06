import pygame

import random

from os import path

from utils.constants import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    IMG_DIR,
    BLACK
)


allowed_speed = list(range(6, 7))
class Superbullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path.join(IMG_DIR, "superbullet.png")).convert()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.choice(allowed_speed)
        self.speedx = random.choice(allowed_speed)

    def update(self):
        if self.rect.bottom < 0:
            self.kill()
        self.rect.x = self.rect.x + self.speedx
        self.rect.y = self.rect.y + self.speedy
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.speedx = random.choice(allowed_speed) * -1
        if self.rect.left < 0:
            self.rect.left = 0
            self.speedx = random.choice(allowed_speed)
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.speedy = random.choice(allowed_speed) * -1
        if self.rect.top < 0:
            self.rect.top = 0
            self.speedy = random.choice(allowed_speed)