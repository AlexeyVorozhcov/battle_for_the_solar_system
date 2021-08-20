from space_objects.base import *
from random import randint
from space_objects.status_health import *
import flying_objects


class Bomb_01(Space_Object):
    name = 'bomb_01'  # имя
    type = 'bomb'  # тип
    image = load_image('Data/meteorits/bomb_01.png')  # изображение объекта
    mask = pygame.mask.from_surface(image)  # маска объекта
    general_direction = Direction.D_LEFT  # основное направление
    direction = Direction.D_LEFT  # текущее направление
    speed = 2  # скорость движения
    health = 1  # здоровье
    max_health = health  # максимальное здоровье
    points = 0  # собранные очки
    value = 10  # сколько очков отдаст при уничтожении
    damage = 1 # какой урон наносит при столкновении
    type_explosion = 5  # уничтожение (номер анимации)
    sounds_pack = get_sound_pack('Data/Sound/02_bobms')


    def __init__(self, x, y):
        super().__init__(allsprites_group, x, y)
        self.sound_explosion = random.choice(self.sounds_pack)  # звук при уничтожении (файл)


class Bomb_02(Bomb_01):
    name = 'bomb_02'  # имя
    image = load_image('Data/meteorits/bomb_02.png')  # изображение объекта
    mask = pygame.mask.from_surface(image)  # маска объекта
    speed = 1  # скорость движения
    health = 7  # здоровье
    max_health = health  # максимальное здоровье
    value = 0  # сколько очков отдаст при уничтожении
    damage = 3  # какой урон наносит при столкновении
    type_explosion = 2  # уничтожение (номер анимации)
    sounds_pack = get_sound_pack('Data/Sound/02_bobms')


class Meteorit_01(Space_Object):
    name = 'meteorit_01'  # имя
    type = 'bomb'  # тип
    images = get_load_images('Data/meteorits/01', '.png', 0, 0)
    masks = get_mask_from_list_of_images(images)
    general_direction = Direction.D_LEFT  # основное направление
    direction = Direction.D_LEFT  # текущее направление
    speed = 4  # скорость движения
    health = 1  # здоровье
    max_health = health  # максимальное здоровье
    points = 0  # собранные очки
    value = 20  # сколько очков отдаст при уничтожении
    damage = 1 # какой урон наносит при столкновении
    type_explosion = 3  # уничтожение (номер анимации)
    sounds_pack = get_sound_pack('Data/Sound/01_meteorits')


    def __init__(self, x, y):
        super().__init__(allsprites_group, x, y)
        rnd = randint(0, len(self.images) - 1)
        self.image = self.images[rnd]  # изображение объекта
        self.mask = self.masks[rnd]  # маска объекта
        self.sound_explosion = random.choice(self.sounds_pack)  # звук при уничтожении (файл)

class Meteorit_02(Meteorit_01):
    name = 'meteorit_02'  # имя
    type = 'bomb'  # тип
    images = get_load_images('Data/meteorits/02', '.png', 0, 0)
    masks = get_mask_from_list_of_images(images)
    rnd = randint(0, len(images)-1)
    image = images[rnd]  # изображение объекта
    mask = masks[rnd]  # маска объекта
    speed = 3  # скорость движения
    health = 2  # здоровье
    max_health = health  # максимальное здоровье
    points = 0  # собранные очки
    value = 10  # сколько очков отдаст при уничтожении
    damage = 1  # какой урон наносит при столкновении
    type_explosion = 3  # уничтожение (номер анимации)
    sounds_pack = get_sound_pack('Data/Sound/01_meteorits')


class Meteorit_boss_pluton(Space_Object):
    name = 'meteorit_boss_pluton'  # имя
    type = 'bomb'  # тип
    image = load_image('Data/meteorits/boss_pluton.png')  # изображение объекта
    mask = pygame.mask.from_surface(image)  # маска объекта
    general_direction = Direction.D_LEFT  # основное направление
    direction = Direction.D_LEFT  # текущее направление
    speed = 1  # скорость движения
    health = 80  # здоровье
    max_health = health  # максимальное здоровье
    points = 0  # собранные очки
    value = 250  # сколько очков отдаст при уничтожении
    damage = 1  # какой урон наносит при столкновении
    type_explosion = 4  # уничтожение (номер анимации)
    is_couse_shaking = True
    is_couse_trophy = 90
    sounds_pack = get_sound_pack('Data/Sound/04_big_opponents')
    is_boss = True

    def __init__(self, x, y, health_alternative=0):
        super().__init__(allsprites_group, x, y)
        self.status_health = Scale_of_XP(self, (255, 36, 0))  # полоска здоровья (объект)
        self.sound_explosion = random.choice(self.sounds_pack)  # звук при уничтожении (файл)
        if health_alternative!=0:
            self.health = health_alternative
            self.max_health = self.health

class Flying_meteorites(flying_objects.Flying_object):
    image1 = mydef.load_image('Data/meteorits/01/01.png')
    image2 = mydef.load_image('Data/meteorits/01/01.png')
    image3 = mydef.load_image('Data/meteorits/01/01.png')
    bonus_pack = [Meteorit_01, Meteorit_02]

class Boss_Saturn(Meteorit_boss_pluton):
    name = 'meteorit_boss_saturn'  # имя
    type = 'opponent'  # тип
    image = load_image('Data/opponents/06_saturn/big_boss.png', -3, -3)  # изображение объекта
    mask = pygame.mask.from_surface(image)  # маска объекта
    health = 110  # здоровье
    max_health = health  # максимальное здоровье


    def update(self):
        super().update()
        if self.health%30 == 0:
            self.health -= 1
            if self.sound_explosion!=None:
                self.sound_explosion.play()
            for i in range(2):
                Flying_meteorites(self.rect.centerx, self.rect.centery, random.randint(10, 80), random.randint(330, 350), 7)
                Flying_meteorites(self.rect.centerx, self.rect.centery, random.randint(280, 350), random.randint(330, 350),-7)
                Flying_meteorites(self.rect.centerx, self.rect.centery, random.randint(100, 170), random.randint(330, 350), 7)
                Flying_meteorites(self.rect.centerx, self.rect.centery, random.randint(190, 260), random.randint(330, 350), -7)




class Fast_Meteorit_01(Meteorit_01):
    speed=6
    points = 0

class Fast_Meteorit_02(Meteorit_02):
    speed = 6
    points = 0




