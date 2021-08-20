from space_objects.base import *
from random import randint
from space_objects.sounds import *
from mydef import *
from math import tan, pi, cos
import public_vars




class Bonus_shot(Space_Object):
    name = 'bonus_shot'  # имя
    type = 'bonus'  # тип
    image = load_image('Data/bonuses/Ammunition_Icon.png')  # изображение объекта
    mask = pygame.mask.from_surface(image)  # маска объекта
    general_direction = Direction.D_LEFT  # основное направление
    direction = Direction.D_LEFT  # текущее направление
    speed = 2  # скорость движения
    health = 0  # здоровье
    max_health = health  # максимальное здоровье
    points = 0  # собранные очки
    value = 200  # сколько патронов отдаст при уничтожении
    damage = 0 # какой урон наносит при столкновении
    type_explosion = 2  # уничтожение (номер анимации)
    sounds_pack = get_sound_pack('Data/Sound/05_bonus_shots')

    def __init__(self, x, y):
        super().__init__(allsprites_group, x, y)
        self.start_y = y
        self.sound_explosion = random.choice(self.sounds_pack)  # звук при уничтожении (файл)

    def to_move(self):
        super().to_move()
        self.rect.y = 10 * cos(0.10 * self.num_step) + self.start_y

class Bonus_health(Bonus_shot):
    name = 'bonus_health'  # имя
    type = 'bonus'  # тип
    image = load_image('Data/bonuses/HP_Icon.png')  # изображение объекта
    mask = pygame.mask.from_surface(image)  # маска объекта
    value = 20  # сколько очков отдаст при уничтожении
    sounds_pack = get_sound_pack('Data/Sound/06_bonus_health')

class Bonus_protect(Bonus_shot):
    name = 'bonus_protect'  # имя
    type = 'bonus'  # тип
    image = load_image('Data/bonuses/Armor_Icon.png')  # изображение объекта
    mask = pygame.mask.from_surface(image)  # маска объекта
    value = 20  # сколько очков отдаст при уничтожении
    sounds_pack = get_sound_pack('Data/Sound/07_bonus_protect')

class Bonus_crystall_small(Bonus_shot):
    name = 'crystall_small'  # имя
    type = 'bonus_crystall'  # тип
    images = get_load_images('Data/bonuses/01', '.png', 0, 0)
    masks = get_mask_from_list_of_images(images)

    general_direction = Direction.D_LEFT  # основное направление
    direction = Direction.D_LEFT  # текущее направление
    speed = 2  # скорость движения
    health = 0  # здоровье
    max_health = health  # максимальное здоровье
    points = 0  # собранные очки
    value = 100  # сколько очков отдаст при уничтожении
    damage = 0 # какой урон наносит при столкновении
    type_explosion = 0  # уничтожение (номер анимации)
    sounds_pack = get_sound_pack('Data/Sound/08_bonus_small')


    def __init__(self, x, y):
        super().__init__(x, y)
        rnd = randint(0, len(self.images) - 1)
        self.image = self.images[rnd]  # изображение объекта
        self.mask = self.masks[rnd]  # маска объекта


class Bonus_crystall_big(Bonus_crystall_small):
    name = 'crystall_big'  # имя
    type = 'bonus_crystall'  # тип
    images = get_load_images('Data/bonuses/02', '.png', 0, 0)
    masks = get_mask_from_list_of_images(images)
    rnd = randint(0, len(images)-1)
    image = images[rnd]  # изображение объекта
    mask = masks[rnd]  # маска объекта
    value = 250  # сколько очков отдаст при уничтожении
    sounds_pack = get_sound_pack('Data/Sound/09_bonus_big')

class Bonus_shot_double(Bonus_shot):
    name = 'bonus_shot_double'  # имя
    type = 'bonus'  # тип
    image = load_image('Data/Ammunition_Icon_double.png')  # изображение объекта
    mask = pygame.mask.from_surface(image)  # маска объекта
    sounds_pack = get_sound_pack('Data/Sound/05_bonus_shots')

class Bonus_shot_fast(Bonus_shot):
    name = 'bonus_shot_fast'  # имя
    type = 'bonus'  # тип
    image = load_image('Data/Ammunition_fast.png')  # изображение объекта
    mask = pygame.mask.from_surface(image)  # маска объекта
    sounds_pack = get_sound_pack('Data/Sound/05_bonus_shots')

class Bonus_atom_shot(Bonus_shot):
    name = 'bonus_atom_shot'  # имя
    type = 'bonus'  # тип
    image = load_image('Data/Nuke_Icon.png')  # изображение объекта
    mask = pygame.mask.from_surface(image)  # маска объекта
    sounds_pack = get_sound_pack('Data/Sound/05_bonus_shots')

public_vars.all_bonuses = [Bonus_shot, Bonus_health, Bonus_protect, Bonus_crystall_small, Bonus_crystall_big, Bonus_shot_double]
public_vars.chance_trophy = [50, 20, 15, 5, 5, 5]



