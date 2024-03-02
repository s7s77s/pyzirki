import pygame
import os
import sys
import random

pygame.init()
current_path = os.path.dirname(__file__)
os.chdir(current_path)
WIDTH = 1200
HEIGHT = 800
FPS = 60
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('pu')

from loader import *


class Food(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.centerx = pos[0]
        self.rect.centery = pos[1]

    def update(self):
        pass


class Enemy1(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speed = 1
        self.speed = random.randint(-5, 5)

    def update(self):
        pass


class Enemy2(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speed = 1
        self.speed = random.randint(-5, 5)

    def update(self):
        pass


class Player(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speed = 5

    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            self.rect.y -= self.speed
        if key[pygame.K_s]:
            self.rect.y += self.speed
        if key[pygame.K_d]:
            self.rect.x += self.speed
        if key[pygame.K_a]:
            self.rect.x -= self.speed

    def update(self):
        self.move()
        if pygame.sprite.spritecollide(self, food_group, True):
            self.image = pygame.transform.rotozoom(self.image, 0, 1.05)
            self.pos = self.rect.center
            self.rect = self.image.get_rect()
            self.rect.center = self.pos


class Spawn():
    def __init__(self):
        self.timer = 0

    def update(self):
        if len(food_group) < 20:
            pos = (random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 100))
            food = Food(food_image, pos)
            food_group.add(food)
        if len(enemy_1_group) < 7:
            pos = (random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 100))
            enemy1 = Enemy1(enemy1_image, pos)
            enemy_1_group.add(enemy1)


def restart():
    global player_group, food_group, enemy_1_group, enemy_2_group, spawn
    player = Player(player_image, (300, 400))
    player_group = pygame.sprite.Group()
    player_group.add(player)
    food_group = pygame.sprite.Group()
    enemy_1_group = pygame.sprite.Group()
    enemy_2_group = pygame.sprite.Group()
    spawn = Spawn()


def lvl_game():
    sc.fill('grey')
    food_group.update()
    food_group.draw(sc)
    player_group.update()
    player_group.draw(sc)
    enemy_1_group.update()
    enemy_1_group.draw(sc)
    spawn.update()
    pygame.display.update()


restart()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    lvl_game()
    clock.tick(FPS)
