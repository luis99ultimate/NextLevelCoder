import pygame

import random

from utils.constants import (
    SCREEN_WIDTH,
    BLACK,
    IMG_DIR
)

from os import path

allowed_speed = list(range(3, 4))
class Powerup(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path.join(IMG_DIR, "powerup.png")).convert()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.top = 0
        self.speedy = random.choice(allowed_speed)

    def update(self):
        self.rect.y = self.rect.y + self.speedy