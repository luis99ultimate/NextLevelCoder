import pygame

from components.ball import Ball

from components.player import Player

from components.powerup import Powerup

from components.dangerouslaser import Dangerous_laser

from components.rightlaser import Right_laser

from utils.constants import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    TITLE,
    WHITE,
    IMG_DIR
)

from os import path
from utils.text_utils import draw_text

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background_img = pygame.image.load(path.join(IMG_DIR, "spacefield.png")).convert()
        self.background_img = pygame.transform.scale(self.background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = True
        pygame.mixer.init()
        pygame.mixer.music.load(path.join(IMG_DIR, "town4.mp3"))
        pygame.mixer.music.play(-1)

    def run(self):
        self.create_components()
        #Game loop:
        self.playing = True
        while self.playing:
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()

    def create_components(self):
        self.all_sprites = pygame.sprite.Group()
        self.balls = pygame.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        ball = Ball(1)
        self.all_sprites.add(ball)
        self.balls.add(ball)
        self.powerups = pygame.sprite.Group()
        powerup = Powerup()
        self.all_sprites.add(powerup)
        self.powerups.add(powerup)
        self.dangerouslasers = pygame.sprite.Group()
        dangerouslaser = Dangerous_laser()
        self.all_sprites.add(dangerouslaser)
        self.dangerouslasers.add(dangerouslaser)
        self.rightlasers = pygame.sprite.Group()
        rightlaser = Right_laser()
        self.all_sprites.add(rightlaser)
        self.rightlasers.add(rightlaser)

    def update(self):
        self.all_sprites.update()
        key = pygame.key.get_pressed()
        if key[pygame.K_r]:
            self.playing = False
        hits = pygame.sprite.spritecollide(self.player, self.balls, False)
        if hits:
            self.playing = False
        hits = pygame.sprite.spritecollide(self.player, self.dangerouslasers, False)
        if hits:
            self.playing = False
        hits = pygame.sprite.spritecollide(self.player, self.rightlasers, False)
        if hits:
            self.playing = False
        hits = pygame.sprite.groupcollide(self.balls, self.player.bullets, True, True)
        for hit in hits:
            if hit.size < 4:
                for i in range (0, 2):
                    ball = Ball(hit.size + 1)
                    self.all_sprites.add(ball)
                    self.balls.add(ball)
        power_hit = pygame.sprite.spritecollide(self.player, self.powerups, False)
        if power_hit:
            self.player.super_shoot()

    def events(self):
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 self.playing = False
                 self.running = False
             elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.shoot()

    def draw(self):
        background_rect = self.background_img.get_rect()
        self.screen.blit(self.background_img, background_rect)
        self.all_sprites.draw(self.screen)
        font1 = pygame.font.SysFont("arial", 20, True, False)
        seconds = pygame.time.get_ticks() // 1000
        seconds = str(seconds)
        timer = font1.render(seconds, 0, (WHITE))
        draw_text(self.screen, "Time playing: ", 20, 55, 3)
        draw_text(self.screen, "R key to replay ", 20, 795, 3)
        self.screen.blit(timer, (105, 5))
        pygame.display.flip()

    def show_start_screen(self):
        self.screen.blit(self.background_img, self.background_img.get_rect())
        draw_text(self.screen, "Space Warrior!!", 64, SCREEN_WIDTH/2, SCREEN_HEIGHT/4)
        draw_text(self.screen, "Press Arrow Keys to move and space to shoot", 20, SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        draw_text(self.screen, "Press ENTER key to begin", 20, SCREEN_WIDTH/2, SCREEN_HEIGHT*3/5)
        draw_text(self.screen, "Press R key to replay at any time", 20, SCREEN_WIDTH/2, SCREEN_HEIGHT*4/6)
        pygame.display.flip()
        waiting = True
        while waiting:
            self.clock.tick(60)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RETURN:
                        waiting = False