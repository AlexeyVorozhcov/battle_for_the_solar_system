from space_objects.base import *
from space_objects.guns import *
from space_objects.sounds import *
from space_objects.status_health import *
import flying_objects

class OP_01_neptun(Space_Object):
    name = 'neptun_01'  # имя
    type = 'opponent'  # тип
    image = load_image('Data/opponents/08_neptun/neptun_01.png')  # изображение объекта
    mask = pygame.mask.from_surface(image)  # маска объекта
    general_direction = Direction.D_LEFT  # основное направление
    direction = Direction.D_LEFT  # текущее направление
    speed = 5  # скорость движения
    health = 1  # здоровье
    max_health = health  # максимальное здоровье
    points = 0  # собранные очки
    value = 30  # сколько очков отдаст при уничтожении
    damage = 1 # какой урон наносит при столкновении
    type_explosion = 1  # уничтожение (номер анимации)
    is_couse_trophy = 8
    sounds_pack = get_sound_pack('Data/Sound/03_standart_opponents')


    def __init__(self, x, y):
        super().__init__(allsprites_group, x, y)
        self.sound_explosion = random.choice(self.sounds_pack)  # звук при уничтожении (файл)

class OP_02_neptun(OP_01_neptun):
    name = 'neptun_02'  # имя
    type = 'opponent'  # тип
    image = load_image('Data/opponents/08_neptun/neptun_02.png')  # изображение объекта
    mask = pygame.mask.from_surface(image)  # маска объекта
    general_direction = Direction.D_LEFT  # основное направление
    direction = Direction.D_LEFT  # текущее направление
    speed = 3  # скорость движения
    health = 1  # здоровье
    max_health = health  # максимальное здоровье
    points = 0  # собранные очки
    value = 50  # сколько очков отдаст при уничтожении
    damage = 2 # какой урон наносит при столкновении
    type_explosion = 1  # уничтожение (номер анимации)
    is_couse_trophy = 10
    def __init__(self, x, y):
        super().__init__(x, y)
        self.gun = G05_standart_opponent(self, 5)

class OP_03_neptun(OP_01_neptun):
    name = 'neptun_02'  # имя
    type = 'opponent'  # тип
    image = load_image('Data/opponents/08_neptun/neptun_03.png')  # изображение объекта
    mask = pygame.mask.from_surface(image)  # маска объекта
    general_direction = Direction.D_LEFT  # основное направление
    direction = Direction.D_LEFT  # текущее направление
    speed = 3  # скорость движения
    health = 1  # здоровье
    max_health = health  # максимальное здоровье
    points =0 # собранные очки
    value = 80  # сколько очков отдаст при уничтожении
    damage = 2 # какой урон наносит при столкновении
    type_explosion = 1  # уничтожение (номер анимации)
    is_couse_trophy = 12

    def __init__(self, x, y):
        super().__init__(x, y)
        self.gun = G05_standart_opponent(self, 5)

class OP_04_neptun(OP_01_neptun):
    name = 'neptun_04'  # имя
    type = 'opponent'  # тип
    image = load_image('Data/opponents/08_neptun/neptun_04.png')  # изображение объекта
    mask = pygame.mask.from_surface(image)  # маска объекта
    general_direction = Direction.D_LEFT  # основное направление
    direction = Direction.D_LEFT  # текущее направление
    speed = 4  # скорость движения
    health = 3  # здоровье
    max_health = health  # максимальное здоровье
    points = 0  # собранные очки
    value = 100  # сколько очков отдаст при уничтожении
    damage = 3 # какой урон наносит при столкновении
    type_explosion = 1  # уничтожение (номер анимации)
    is_couse_trophy = 14

    def __init__(self, x, y):
        super().__init__(x, y)
        self.gun = G05_standart_opponent(self, 5)

class OP_01_uran01(OP_01_neptun):
    name = 'uran_01'  # имя
    type = 'opponent'  # тип
    image = load_image('Data/opponents/07_uran/01.png')  # изображение объекта
    mask = pygame.mask.from_surface(image)  # маска объекта
    health = 2  # здоровье
    max_health = health  # максимальное здоровье
    value = 40  # сколько очков отдаст при уничтожении

class OP_02_uran02(OP_02_neptun):
    name = 'uran_02'  # имя
    type = 'opponent'  # тип
    image = load_image('Data/opponents/07_uran/02.png')  # изображение объекта
    mask = pygame.mask.from_surface(image)  # маска объекта
    health = 3  # здоровье
    max_health = health  # максимальное здоровье
    speed = 3  # скорость движения
    value = 100  # сколько очков отдаст при уничтожении
    damage = 3  # какой урон наносит при столкновении

    def __init__(self, x, y):
        super().__init__(x, y)
        self.gun = G06_double_opponent(self, 10)

    def ai_control(self):
        super().ai_control()
        if random_chance([True, False], [4, 96]):
            self.direction = random.choice([Direction.D_LEFT, Direction.D_LEFT, Direction.D_LEFT_UP, Direction.D_UP, Direction.D_RIGTH_UP,
                                            Direction.D_RIGTH, Direction.D_RIGTH_DOWN, Direction.D_DOWN, Direction.D_LEFT_DOWN])
        if self.rect.y <15: self.direction = Direction.D_DOWN
        if self.rect.bottom >HEIGHT_GAMEBOARD-15: self.direction = Direction.D_UP
        if self.rect.centerx < 200: self.direction = Direction.D_RIGTH
        if self.rect.centerx > WIDTH_GAMEBOARD-20: self.direction = Direction.D_LEFT


class OP_03_uran02(OP_02_neptun):
    name = 'uran_03'  # имя
    type = 'opponent'  # тип
    image = load_image('Data/opponents/07_uran/03.png')  # изображение объекта
    mask = pygame.mask.from_surface(image)  # маска объекта
    health = 3  # здоровье
    max_health = health  # максимальное здоровье
    speed = 3  # скорость движения
    value = 150  # сколько очков отдаст при уничтожении
    damage = 3  # какой урон наносит при столкновении

    def __init__(self, x, y):
        super().__init__(x, y)
        self.gun = G061_third_opponent(self, 6)

class OP_04_uran02(OP_03_neptun):
    name = 'uran_04'  # имя
    type = 'opponent'  # тип
    image = load_image('Data/opponents/07_uran/04.png')  # изображение объекта
    mask = pygame.mask.from_surface(image)  # маска объекта
    health = 4  # здоровье
    max_health = health  # максимальное здоровье
    speed = 2  # скорость движения
    value = 200  # сколько очков отдаст при уничтожении
    damage = 5  # какой урон наносит при столкновении

    def __init__(self, x, y):
        super().__init__(x, y)
        self.gun = G05_standart_opponent(self, 6)

    def ai_control(self):
        super().ai_control()
        if random_chance([True, False], [3, 97]):
            self.direction = random.choice(
                [Direction.D_LEFT, Direction.D_LEFT, Direction.D_LEFT_UP, Direction.D_UP, Direction.D_RIGTH_UP,
                 Direction.D_RIGTH, Direction.D_RIGTH_DOWN, Direction.D_DOWN, Direction.D_LEFT_DOWN, Direction.D_STOP])
        if self.rect.y < 10: self.direction = Direction.D_DOWN
        if self.rect.bottom > HEIGHT_GAMEBOARD - 10: self.direction = Direction.D_UP
        if self.rect.x < 300: self.direction = Direction.D_RIGTH
        if self.rect.x > WIDTH_GAMEBOARD-10: self.direction = Direction.D_LEFT

class OP_boss_uran2(OP_04_uran02):
    name = 'boss_uran'  # имя
    type = 'opponent'  # тип
    image = load_image('Data/opponents/07_uran/boss.png')  # изображение объекта
    mask = pygame.mask.from_surface(image)  # маска объекта
    health = 120  # здоровье
    max_health = health  # максимальное здоровье
    speed = 1  # скорость движения
    value = 500  # сколько очков отдаст при уничтожении
    damage = 5  # какой урон наносит при столкновении
    type_explosion = 4  # уничтожение (номер анимации)
    is_couse_shaking = True
    is_couse_trophy = 100
    is_boss = True
    is_may_abroad = True

    def __init__(self, x, y):
        super().__init__(x, y)
        self.gun = G_boss_uran(self, 1000)
        self.status_health = Scale_of_XP(self, (255, 36, 0))  # полоска здоровья (объект)
        self.sound_explosion = get_random_sound('Data/Sound/04_big_opponents')  # звук при уничтожении (файл)


class OP_03_upiter_05(OP_03_uran02):
    name = 'upiter_03'  # имя
    type = 'opponent'  # тип
    image = load_image('Data/opponents/05_upiter/03.png')  # изображение объекта
    mask = pygame.mask.from_surface(image)  # маска объекта
    health = 1  # здоровье
    max_health = health  # максимальное здоровье
    value = 100  # сколько очков отдаст при уничтожении

    def __init__(self, x, y):
        super().__init__(x, y)
        self.gun = G08_cosinus_opponent(self, 5)

class OP_04_upiter_05(OP_04_uran02):
    name = 'upiter_04'  # имя
    type = 'opponent'  # тип
    image = load_image('Data/opponents/05_upiter/04.png')  # изображение объекта
    mask = pygame.mask.from_surface(image)  # маска объекта
    health = 30  # здоровье
    max_health = health  # максимальное здоровье
    is_couse_trophy = 50
    value = 200  # сколько очков отдаст при уничтожении
    def __init__(self, x, y):
        super().__init__(x, y)
        self.gun = G06_double_opponent(self, 6)
        self.speed = 1  # скорость движения

class Flying_opponents(flying_objects.Flying_object):
    image1 = mydef.load_image('Data/shots/04 - main - hard_gun.png')
    image2 = mydef.load_image('Data/shots/04 - main - hard_gun.png')
    image3 = mydef.load_image('Data/shots/04 - main - hard_gun.png')
    bonus_pack = [OP_01_neptun, OP_01_uran01, OP_03_upiter_05]

class OP_Boss_upiter(OP_boss_uran2):
    name = 'boss_upiter'  # имя
    type = 'opponent'  # тип
    image_0 = load_image('Data/opponents/05_upiter/boss.png')
    image = image_0  # изображение объекта
    mask = pygame.mask.from_surface(image)  # маска объекта
    ungle = 0
    speed_rotate = 20
    timer_rotate = pygame.time.get_ticks()
    is_couse_trophy = 100
    health = 120  # здоровье
    max_health = health  # максимальное здоровье
    value = 700  # сколько очков отдаст при уничтожении

    def update(self):
        super().update()
        if mydef.check_timer(self.timer_rotate, self.speed_rotate):
            self.ungle +=1
            if self.ungle>360: self.ungle = 1
            self.image = pygame.transform.rotate(self.image_0, self.ungle)
            self.rect = self.image.get_rect(center=self.rect.center)
            self.mask = pygame.mask.from_surface(self.image)
            self.timer_rotate = pygame.time.get_ticks()
            if self.ungle%180 ==0:
                self.ungle += 1
                for i in range(2):
                    Flying_opponents(self.rect.centerx, self.rect.centery, random.randint(10, 80),
                                      random.randint(330, 350), 7)
                    Flying_opponents(self.rect.centerx, self.rect.centery, random.randint(280, 350),
                                      random.randint(330, 350), -7)
                    Flying_opponents(self.rect.centerx, self.rect.centery, random.randint(100, 170),
                                      random.randint(330, 350), 7)
                    Flying_opponents(self.rect.centerx, self.rect.centery, random.randint(190, 260),
                                      random.randint(330, 350), -7)



