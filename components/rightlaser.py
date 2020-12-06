import pygame

import random

from utils.constants import (
    BLACK,
    SCREEN_WIDTH,
    IMG_DIR
)

from os import path

allowed_speed = list(range(8, 10))
allowed_place = list(range(330, 460))
class Right_laser(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path.join(IMG_DIR, "dangerouslaser.png")).convert()
        self.image = pygame.transform.scale(self.image, (40, 20))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.right = SCREEN_WIDTH
        self.rect.top = random.choice((allowed_place))
        self.speedx = random.choice((allowed_speed))

    def update(self):
        self.rect.x = self.rect.x - self.speedx