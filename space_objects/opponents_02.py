import pygame
from space_objects.base import Direction
import space_objects.opponents
from mydef import load_image, random_chance
import random
from public_vars import HEIGHT_GAMEBOARD, WIDTH_GAMEBOARD
from public_vars import allsprites_group
from space_objects.guns import *
import flying_objects
from space_objects.bombs_meteorits import *
from space_objects.bonuses import *

class OP_01_Mars (space_objects.opponents.OP_01_neptun):
    name = 'mars_01'  # имя
    type = 'opponent'  # тип
    image = load_image('Data/opponents/04_mars/01.png')  # изображение объекта
    mask = pygame.mask.from_surface(image)  # маска объекта
    speed = 6
    value = 30  # сколько очков отдаст при уничтожении

    def __init__(self, x, y):
        super().__init__(x, y)
        self.sound_explosion = random.choice(self.sounds_pack)  # звук при уничтожении (файл)

class OP_02_Mars (space_objects.opponents.OP_02_neptun):
    name = 'mars_02'  # имя
    type = 'opponent'  # тип
    image = load_image('Data/opponents/04_mars/02.png')  # изображение объекта
    mask = pygame.mask.from_surface(image)  # маска объекта
    value = 100  # сколько очков отдаст при уничтожении

    def __init__(self, x, y):
        super().__init__(x, y)
        self.sound_explosion = random.choice(self.sounds_pack)  # звук при уничтожении (файл)

    def ai_control(self):
        super().ai_control()
        if random_chance([True, False], [3, 97]):
            self.direction = random.choice([Direction.D_LEFT, Direction.D_LEFT_UP, Direction.D_LEFT_DOWN])
        if self.rect.y < 20: self.direction = Direction.D_LEFT_DOWN
        if self.rect.bottom > HEIGHT_GAMEBOARD-20: self.direction = Direction.D_LEFT_UP

class OP_03_Mars (space_objects.opponents.OP_03_uran02):
    name = 'mars_03'  # имя
    type = 'opponent'  # тип
    image = load_image('Data/opponents/04_mars/03.png')  # изображение объекта
    mask = pygame.mask.from_surface(image)  # маска объекта
    value = 130  # сколько очков отдаст при уничтожении

    def __init__(self, x, y):
        super().__init__(x, y)
        self.sound_explosion = random.choice(self.sounds_pack)  # звук при уничтожении (файл)
        self.gun = G06_double_opponent(self, 6)


class OP04_Mars(OP_02_Mars):
    name = 'mars_04'  # имя
    type = 'opponent'  # тип
    image = load_image('Data/opponents/04_mars/04.png')  # изображение объекта
    mask = pygame.mask.from_surface(image)  # маска объекта
    speed = 2
    health = 10
    max_health = health
    is_couse_trophy = 95  # вероятность выдачи трофея после смерти
    value = 200  # сколько очков отдаст при уничтожении

    def __init__(self, x, y):
        super().__init__(x, y)
        self.sound_explosion = random.choice(self.sounds_pack)  # звук при уничтожении (файл)
        self.gun = G07_fast_opponent(self, 3)

class Flying_opponents_mars(flying_objects.Flying_object):
    image1 = mydef.load_image('Data/shots/04 - main - hard_gun.png')
    image2 = mydef.load_image('Data/shots/04 - main - hard_gun.png')
    image3 = mydef.load_image('Data/shots/04 - main - hard_gun.png')
    bonus_pack = [OP_01_Mars]

class OP05_Mars(OP_01_Mars):
    name = 'mars_05'  # имя
    type = 'opponent'  # тип
    image = load_image('Data/opponents/04_mars/05.png')  # изображение объекта
    mask = pygame.mask.from_surface(image)  # маска объекта
    speed = 1
    health = 25
    max_health = health
    is_couse_trophy = 10  # вероятность выдачи трофея после смерти
    value = 300  # сколько очков отдаст при уничтожении

    def __init__(self, x, y):
        super().__init__(x, y)
        self.sound_explosion = random.choice(self.sounds_pack)  # звук при уничтожении (файл)
        self.gun = G061_third_opponent(self, 6)

    def ai_control(self):
        super().ai_control()
        if random_chance([True, False], [3, 97]):
            self.direction = random.choice([Direction.D_LEFT, Direction.D_LEFT, Direction.D_LEFT_UP, Direction.D_UP, Direction.D_RIGTH_UP,
                                            Direction.D_RIGTH, Direction.D_RIGTH_DOWN, Direction.D_DOWN, Direction.D_LEFT_DOWN])
        if self.rect.y <1: self.direction = Direction.D_DOWN
        if self.rect.bottom >HEIGHT_GAMEBOARD: self.direction = Direction.D_UP
        if self.rect.x < 50: self.direction = Direction.D_RIGTH

        if random_chance([True, False], [2, 98]):
            for i in range(1):
                Flying_opponents_mars(self.rect.centerx, self.rect.centery, random.randint(10, 80),
                                 random.randint(330, 350), 5)
                Flying_opponents_mars(self.rect.centerx, self.rect.centery, random.randint(280, 350),
                                 random.randint(330, 350), -5)
                Flying_opponents_mars(self.rect.centerx, self.rect.centery, random.randint(100, 170),
                                 random.randint(330, 350), 5)
                Flying_opponents_mars(self.rect.centerx, self.rect.centery, random.randint(190, 260),
                                 random.randint(330, 350), -5)



class OP_06_Mars(OP_01_Mars):
    name = 'mars_06'  # имя
    type = 'opponent'  # тип
    image = load_image('Data/opponents/04_mars/06.png')  # изображение объекта
    mask = pygame.mask.from_surface(image)  # маска объекта
    speed = 4
    value = 100  # сколько очков отдаст при уничтожении

    def __init__(self, x, y):
        super().__init__(x, y)
        self.start_y = y
        self.sound_explosion = random.choice(self.sounds_pack)  # звук при уничтожении (файл)
        self.gun = G08_cosinus_opponent(self, 1)

    def to_move(self):
        super().to_move()
        self.rect.y = 40 * cos(0.05 * self.num_step) + self.start_y

class Flying_opponents_mars_boss(flying_objects.Flying_object):
    image1 = mydef.load_image('Data/shots/04 - main - hard_gun.png')
    image2 = mydef.load_image('Data/shots/04 - main - hard_gun.png')
    image3 = mydef.load_image('Data/shots/04 - main - hard_gun.png')
    bonus_pack = [Bomb_01, Bomb_01, Bomb_01, Bomb_01,Bonus_crystall_small, Bonus_crystall_big, Bonus_shot, Bonus_protect ]

class OP_06_Boss_mars(space_objects.opponents.OP_boss_uran2):
    name = 'boss_uran'  # имя
    type = 'opponent'  # тип
    image = load_image('Data/opponents/04_mars/boss.png')  # изображение объекта
    mask = pygame.mask.from_surface(image)  # маска объекта
    is_may_abroad = True
    speed = 1
    value = 800  # сколько очков отдаст при уничтожении

    def ai_control(self):
        super().ai_control()
        if random_chance([True, False], [1, 99]):
            self.direction = random.choice([Direction.D_LEFT, Direction.D_LEFT, Direction.D_LEFT_UP, Direction.D_UP, Direction.D_RIGTH_UP,
                                            Direction.D_RIGTH, Direction.D_RIGTH_DOWN, Direction.D_DOWN, Direction.D_LEFT_DOWN, Direction.D_STOP])
        if self.rect.y <1: self.direction = Direction.D_DOWN
        if self.rect.bottom >HEIGHT_GAMEBOARD: self.direction = Direction.D_UP
        if self.rect.x <300: self.direction = Direction.D_RIGTH

        if random_chance([True, False], [2, 110]):
            for i in range(1):
                Flying_opponents_mars_boss(self.rect.centerx, self.rect.centery, random.randint(10, 80),
                                 random.randint(900, 1000), 5)
                Flying_opponents_mars_boss(self.rect.centerx, self.rect.centery, random.randint(280, 350),
                                 random.randint(900, 1000), -5)
                Flying_opponents_mars_boss(self.rect.centerx, self.rect.centery, random.randint(100, 170),
                                 random.randint(900, 1000), 5)
                Flying_opponents_mars_boss(self.rect.centerx, self.rect.centery, random.randint(190, 260),random.randint(900, 1000), -5)


class OP_01_Earth(OP_01_Mars):
    name = 'earth_01'  # имя
    type = 'opponent'  # тип
    image = load_image('Data/opponents/03_earth/01.png')  # изображение объекта
    mask = pygame.mask.from_surface(image)  # маска объекта
    speed = 6
    value = 100  # сколько очков отдаст при уничтожении

    def __init__(self, x, y):
        super().__init__(x, y)
        self.sound_explosion = random.choice(self.sounds_pack)  # звук при уничтожении (файл)

class OP_02_Earth(OP_02_Mars):
    name = 'earth_02'  # имя
    type = 'opponent'  # тип
    image = load_image('Data/opponents/03_earth/02.png')  # изображение объекта
    mask = pygame.mask.from_surface(image)  # маска объекта
    speed = 4
    value = 150  # сколько очков отдаст при уничтожении

    def __init__(self, x, y):
        super().__init__(x, y)
        self.sound_explosion = random.choice(self.sounds_pack)  # звук при уничтожении (файл)

class OP_03_Earth(OP_03_Mars):
    name = 'earth_03'  # имя
    type = 'opponent'  # тип
    image = load_image('Data/opponents/03_earth/03.png')  # изображение объекта
    mask = pygame.mask.from_surface(image)  # маска объекта
    speed = 3
    value = 200  # сколько очков отдаст при уничтожении

    def __init__(self, x, y):
        super().__init__(x, y)
        self.sound_explosion = random.choice(self.sounds_pack)  # звук при уничтожении (файл)
        self.gun = G10_homing_opponent(self, 3)

class OP_04_Earth(OP04_Mars):
    name = 'earth_04'  # имя
    type = 'opponent'  # тип
    image = load_image('Data/opponents/03_earth/04.png')  # изображение объекта
    mask = pygame.mask.from_surface(image)  # маска объекта
    health = 4
    max_health = health
    speed = 4
    value = 250  # сколько очков отдаст при уничтожении

    def __init__(self, x, y):
        super().__init__(x, y)
        self.sound_explosion = random.choice(self.sounds_pack)  # звук при уничтожении (файл)
        self.gun = G10_homing_opponent(self, 5)

class OP_05_Earth(OP05_Mars):
    name = 'earth_05'  # имя
    type = 'opponent'  # тип
    image = load_image('Data/opponents/03_earth/05.png')  # изображение объекта
    mask = pygame.mask.from_surface(image)  # маска объекта
    speed = 2
    value = 300  # сколько очков отдаст при уничтожении

    def __init__(self, x, y):
        super().__init__(x, y)
        self.sound_explosion = random.choice(self.sounds_pack)  # звук при уничтожении (файл)

class Flying_opponents_earth(flying_objects.Flying_object):
    image1 = mydef.load_image('Data/shots/04 - main - hard_gun.png')
    image2 = mydef.load_image('Data/shots/04 - main - hard_gun.png')
    image3 = mydef.load_image('Data/shots/04 - main - hard_gun.png')
    bonus_pack = [OP_01_Earth, OP_02_Earth]

class OP_stantion_Earth(OP_01_Earth):
    name = 'earth_05'  # имя
    type = 'opponent'  # тип
    image_0 = load_image('Data/opponents/03_earth/stantion.png')
    image = image_0  # изображение объекта
    mask = pygame.mask.from_surface(image)  # маска объекта
    ungle = 0
    speed_rotate = 20
    timer_rotate = pygame.time.get_ticks()
    is_couse_trophy = 50
    health = 30  # здоровье
    max_health = health  # максимальное здоровье
    value = 300  # сколько очков отдаст при уничтожении
    speed = 1

    def update(self):
        super().update()
        if mydef.check_timer(self.timer_rotate, self.speed_rotate):
            self.ungle += 1
            if self.ungle > 360: self.ungle = 1
            self.image = pygame.transform.rotate(self.image_0, self.ungle)
            self.rect = self.image.get_rect(center=self.rect.center)
            self.mask = pygame.mask.from_surface(self.image)
            self.timer_rotate = pygame.time.get_ticks()
            if self.ungle%200 ==0:
                self.ungle += 1
                for i in range(1):
                    Flying_opponents_earth(self.rect.centerx, self.rect.centery, random.randint(10, 80),
                                      random.randint(1000, 1000), 7)
                    Flying_opponents_earth(self.rect.centerx, self.rect.centery, random.randint(280, 350),
                                      random.randint(1000, 1000), -7)
                    Flying_opponents_earth(self.rect.centerx, self.rect.centery, random.randint(100, 170),
                                      random.randint(1000, 1000), 7)
                    Flying_opponents_earth(self.rect.centerx, self.rect.centery, random.randint(190, 260),
                                      random.randint(1000, 1000), -7)


class OP_boss1_Earth(OP_01_Earth):
    name = 'earth_boss1'  # имя
    type = 'opponent'  # тип
    image = load_image('Data/opponents/03_earth/boss1.png')  # изображение объекта
    mask = pygame.mask.from_surface(image)  # маска объекта
    speed = 1
    value = 1000  # сколько очков отдаст при уничтожении
    health = 300
    max_health = health
    is_boss = True
    damage = 6  # какой урон наносит при столкновении
    type_explosion = 4  # уничтожение (номер анимации)
    is_couse_shaking = True
    is_couse_trophy = 100
    is_make_boss2 = False

    def __init__(self, x, y):
        super().__init__(x, y)
        self.gun = G09_hard_opponent(self, 100)
        self.status_health = Scale_of_XP(self, (255, 36, 0))  # полоска здоровья (объект)
        self.sound_explosion = get_random_sound('Data/Sound/04_big_opponents')  # звук при уничтожении (файл)

    def ai_control(self):
        super().ai_control()
        if self.health<2 and not self.is_make_boss2:
            OP_boss2_Earth(WIDTH_GAMEBOARD -1, 50)
            self.is_make_boss2 = True
        if random_chance([True, False], [1, 99]):
            self.direction = random.choice([Direction.D_LEFT, Direction.D_UP, Direction.D_RIGTH_UP,
                                            Direction.D_RIGTH, Direction.D_RIGTH_DOWN, Direction.D_DOWN, Direction.D_LEFT_DOWN, Direction.D_STOP])
        if self.rect.y <1: self.direction = Direction.D_DOWN
        if self.rect.bottom >HEIGHT_GAMEBOARD: self.direction = Direction.D_UP
        if self.rect.x <300: self.direction = Direction.D_RIGTH
        if self.rect.x > WIDTH_GAMEBOARD -10: self.direction = Direction.D_LEFT

        if random_chance([True, False], [2, 150]):
            for i in range(1):
                Flying_opponents_mars_boss(self.rect.left, self.rect.centery, random.randint(10, 80),
                                 random.randint(900, 1000), 5)
                Flying_opponents_mars_boss(self.rect.left, self.rect.centery, random.randint(280, 350),
                                 random.randint(900, 1000), -5)
                Flying_opponents_mars_boss(self.rect.left, self.rect.centery, random.randint(100, 170),
                                 random.randint(900, 1000), 5)
                Flying_opponents_mars_boss(self.rect.left, self.rect.centery, random.randint(190, 260),random.randint(900, 1000), -5)



class OP_boss2_Earth(OP_boss1_Earth):
    name = 'earth_boss2'  # имя
    type = 'opponent'  # тип
    image = load_image('Data/opponents/03_earth/boss2.png')  # изображение объекта
    mask = pygame.mask.from_surface(image)  # маска объекта
    speed = 1
    value = 1500  # сколько очков отдаст при уничтожении
    health = 200
    max_health = health
    is_boss = True
    damage = 6  # какой урон наносит при столкновении
    type_explosion = 4  # уничтожение (номер анимации)
    is_couse_shaking = True
    is_couse_trophy = 100
    is_make_boss2 = True
    def __init__(self, x, y):
        super().__init__(x, y)
        self.gun = G09_superhard_opponent(self, 100)
        self.status_health = Scale_of_XP(self, (255, 36, 0))  # полоска здоровья (объект)
        self.sound_explosion = get_random_sound('Data/Sound/04_big_opponents')  # звук при уничтожении (файл)


