from space_objects.opponents_02 import *


class OP_03_Venera(OP_01_Earth):
    name = 'venera_03'  # имя
    type = 'opponent'  # тип
    image = load_image('Data/opponents/02_venera/03.png')  # изображение объекта
    mask = pygame.mask.from_surface(image)  # маска объекта
    speed = 3
    value = 200  # сколько очков отдаст при уничтожении
    health = 4
    max_health = health
    is_couse_trophy = 60  # вероятность выдачи трофея после смерти

    def __init__(self, x, y):
        super().__init__(x, y)
        self.sound_explosion = random.choice(self.sounds_pack)  # звук при уничтожении (файл)
        self.gun = G05_standart_opponent(self, 10)
        self.gun.periodicity = 1200

    def ai_control(self):
        super().ai_control()
        if random_chance([True, False], [5, 95]):
            self.direction = random.choice([Direction.D_LEFT, Direction.D_LEFT, Direction.D_LEFT_UP, Direction.D_UP, Direction.D_RIGTH_UP,
                                            Direction.D_RIGTH, Direction.D_RIGTH_DOWN, Direction.D_DOWN, Direction.D_LEFT_DOWN, Direction.D_STOP])
        if self.rect.y <10: self.direction = Direction.D_DOWN
        if self.rect.bottom >HEIGHT_GAMEBOARD-10: self.direction = Direction.D_UP
        if self.rect.x <300: self.direction = Direction.D_RIGTH
        if self.rect.x > WIDTH_GAMEBOARD - 100: self.direction = Direction.D_LEFT



class OP_04_Venera (OP_03_Venera):
    name = 'venera_04'  # имя
    type = 'opponent'  # тип
    image = load_image('Data/opponents/02_venera/04.png')  # изображение объекта
    mask = pygame.mask.from_surface(image)  # маска объекта
    speed = 4
    value = 300  # сколько очков отдаст при уничтожении
    health = 5
    max_health = health
    def __init__(self, x, y):
        super().__init__(x, y)
        self.sound_explosion = random.choice(self.sounds_pack)  # звук при уничтожении (файл)
        self.gun = G10_homing_opponent (self, 10)
        self.gun.periodicity = 1200

class OP_boss_Venera (OP_03_Venera):
    name = 'boss_venera'  # имя
    type = 'opponent'  # тип
    image = load_image('Data/opponents/02_venera/boss.png')  # изображение объекта
    mask = pygame.mask.from_surface(image)  # маска объекта
    speed = 1
    value = 1000  # сколько очков отдаст при уничтожении
    health = 200
    max_health = health
    is_boss = True
    is_may_abroad = True
    is_couse_shaking = True
    type_explosion = 4  # уничтожение (номер анимации)
    is_couse_trophy = 100
    def __init__(self, x, y):
        super().__init__(x, y)
        self.sound_explosion = random.choice(self.sounds_pack)  # звук при уничтожении (файл)
        self.gun = G11_boss_venera (self, 1000)
        self.status_health = Scale_of_XP(self, (255, 36, 0))  # полоска здоровья (объект)

    def ai_control(self):
        super().ai_control()
        if random_chance([True, False], [2, 98]):
            if self.gun.name == 'boss_venera':
                self.gun = G_boss_uran(self, 100)
                self.gun.periodicity = 1000
                self.gun.speed = 7
            else: self.gun = G11_boss_venera(self, 100)

