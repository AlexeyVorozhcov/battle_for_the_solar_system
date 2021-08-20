import pygame
import space_objects.opponents_venera
import space_objects.opponents
import space_objects.bombs_meteorits
import space_objects.bonuses
from space_objects.guns import *
from mydef import load_image
import random


class OP_01_Mer(space_objects.opponents_venera.OP_01_Mars):
    name = 'mer_01'  # имя
    type = 'opponent'  # тип
    image = load_image('Data/opponents/01_mercury/01.png')  # изображение объекта
    mask = pygame.mask.from_surface(image)  # маска объекта
    speed = 5
    value = 120  # сколько очков отдаст при уничтожении
    health = 4
    max_health = health
    def __init__(self, x, y):
        super().__init__(x, y)
        self.start_y = y
        self.sound_explosion = random.choice(self.sounds_pack)  # звук при уничтожении (файл)
    def to_move(self):
        super().to_move()
        self.rect.y = 60 * cos(0.09 * self.num_step) + self.start_y

class OP_02_Mer(space_objects.opponents.OP_02_uran02):
    name = 'mer_02'  # имя
    type = 'opponent'  # тип
    image = load_image('Data/opponents/01_mercury/02.png')  # изображение объекта
    mask = pygame.mask.from_surface(image)  # маска объекта
    speed = 4
    value = 150  # сколько очков отдаст при уничтожении
    health = 4
    max_health = health
    def __init__(self, x, y):
        super().__init__(x, y)
        self.sound_explosion = random.choice(self.sounds_pack)  # звук при уничтожении (файл)
        self.gun = G05_standart_opponent(self, 6)

class OP_03_Mer(space_objects.opponents.OP_01_neptun):
    name = 'mer_03_alien'  # имя
    type = 'opponent'  # тип
    image = load_image('Data/opponents/01_mercury/03.png')  # изображение объекта
    mask = pygame.mask.from_surface(image)  # маска объекта
    speed = 7
    value = 100  # сколько очков отдаст при уничтожении
    health = 4
    max_health = health
    def __init__(self, x, y):
        super().__init__(x, y)
        self.sound_explosion = random.choice(self.sounds_pack)  # звук при уничтожении (файл)
        self.gun = None
        self.direction = random.choice([Direction.D_LEFT_UP, Direction.D_LEFT_DOWN])
        if self.direction == Direction.D_LEFT_UP:
            self.rect.x = random.randint(WIDTH_GAMEBOARD - 200, WIDTH_GAMEBOARD-1)
            self.rect.y = HEIGHT_GAMEBOARD-1
        else:
            self.rect.x = random.randint(WIDTH_GAMEBOARD - 200, WIDTH_GAMEBOARD-1)
            self.rect.y = 1

class OP_Boss_merc(space_objects.opponents.OP_boss_uran2):
    name = 'boss_merc'  # имя
    type = 'opponent'  # тип
    image = load_image('Data/opponents/01_mercury/boss.png')  # изображение объекта
    mask = pygame.mask.from_surface(image)  # маска объекта
    health = 300  # здоровье
    max_health = health  # максимальное здоровье
    speed = 3  # скорость движения
    value = 1500  # сколько очков отдаст при уничтожении
    damage = 3  # какой урон наносит при столкновении
    b_pack =[space_objects.bombs_meteorits.Meteorit_01,
             space_objects.bombs_meteorits.Meteorit_02,
             space_objects.bonuses.Bonus_shot_fast,
             space_objects.bonuses.Bonus_health,
             space_objects.bonuses.Bonus_protect,
             space_objects.bonuses.Bonus_crystall_big,
             space_objects.bonuses.Bonus_crystall_small,
             OP_02_Mer
             ]

    def __init__(self, x, y):
        super().__init__(x, y)
        self.gun = G07_fast_opponent(self, 1000)
        self.gun.periodicity = 1050
        self.gun.speed = 10

    def ai_control(self):
        super().ai_control()
        if random_chance([True, False], [2, 99]):
            random.choice(self.b_pack)(WIDTH_GAMEBOARD-1, random.randint(1, HEIGHT_GAMEBOARD-1))

