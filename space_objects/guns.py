from space_objects.base import *
from math import cos
import flying_objects


class Shot(Space_Object):
    def __init__(self, master, x, y):
        super().__init__(allsprites_group, x, y)
        self.image = master.image
        self.mask = master.mask
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.name = master.name  # имя
        self.type = master.type  # тип
        self.general_direction = master.general_direction  # основное направление
        self.direction = master.direction  # текущее направление
        self.speed = master.speed # скорость движения
        self.health = master.health  # здоровье
        self.max_health = self.health  # максимальное здоровье
        self.points = 0  # собранные очки
        self.value = 0  # сколько очков отдаст при уничтожении
        self.damage = master.damage  # какой урон наносит при столкновении
        self.type_explosion = master.type_explosion  # уничтожение (номер анимации)
        self.sound_explosion = master.sound_explosion  # звук при уничтожении (файл)
        self.master = master


class Shot_cosinus(Shot):
    def __init__(self, master, x, y):
        super().__init__(master, x, y)
        self.start_y = y

    def to_move(self):
        super().to_move()
        self.rect.y = 20 * cos(0.20 * self.num_step) + self.start_y

class Shot_homing(Shot):
    def __init__(self, master, x0, y0, x1, y1, speed ):
        super().__init__(master, x0, y0)
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.x = 0
        self.y = 0
        self.t = 0
        self.step = 1 / speed
        self.rect.x = self.x
        self.rect.y = self.y
        self.is_stop = False

    def update(self):
        if not self.is_stop:
            self.t += self.step
            if self.t > 1: self.is_stop = True
            self.x = self.x0 + (self.x1-self.x0)*self.t
            self.y = self.y0 + (self.y1-self.y0)*self.t
            # print((self.t, self.x, self.y))
            self.rect.x = self.x
            self.rect.y = self.y
        else:
            self.kill()




class Shot_hard(Shot_homing):
    pass
    # def to_destruction(self, uron=1):
    #     super().to_destruction(uron=1)
    #     # вставить код создания объекта супервзрыва

class Shot_Atom(Shot):

    def __init__(self, master, x, y):
        super().__init__(master, x, y)
        self.type_explosion = 7  # уничтожение (номер анимации)
        self.damage = 10



class G01_standart():
    name = 'standart_gun'
    periodicity = 60 # частота выстрелов (чем меньше значение, тем выше скорострельность)
    periodcity_time = pygame.time.get_ticks()
    rate = 1 # сколько снарядов расходуется за один выстрел
    is_shooting = False
    type = 'shot_main'  # тип
    image = load_image('Data/shots/01 - main - standart_gun.png')  # изображение объекта
    mask = pygame.mask.from_surface(image)  # маска объекта
    speed = 12  # скорость движения
    health = 1  # здоровье
    max_health = health  # максимальное здоровье
    damage = 1  # какой урон наносит при столкновении
    type_explosion = 0
    sound_explosion = None

    def __init__(self, master, shots):
        self.master = master
        self.shots = shots  # количество снарядов
        self.general_direction = master.general_direction  # основное направление
        self.direction = master.general_direction  # текущее направление

    def get_pos_gun(self):
        x = 0
        if self.general_direction == Direction.D_RIGTH:
            x = self.master.rect.right + 1
        else:
            x = self.master.rect.left - 1
        y = self.master.rect.centery
        return x, y

    def make_shot(self, x, y):
            Shot(self, x, y)

    def to_shoot(self):
        if self.is_shooting and self.shots > 0:
            if check_timer(self.periodcity_time, self.periodicity):
                x, y = self.get_pos_gun()
                self.make_shot(x, y)
                self.periodcity_time = pygame.time.get_ticks()
                self.shots -= self.rate
                if self.shots<=0: self.shots=0

class G02_double(G01_standart):
    name = 'double_gun'
    rate = 2  # сколько снарядов расходуется за один выстрел

    def make_shot(self, x, y):
        Shot(self, x, y-13)
        Shot(self, x, y+13)

class G03_fast(G01_standart):
    name = 'fast_gun'
    speed = 15
    damage = 2  # какой урон наносит при столкновении
    rate = 2  # сколько снарядов расходуется за один выстрел
    image = load_image('Data/shots/03 - main - fast_gun.png')  # изображение объекта
    mask = pygame.mask.from_surface(image)  # маска объекта

class G04_Atom(G01_standart):
    name = 'atom_gun'
    speed = 7
    damage = 3  # какой урон наносит при столкновении
    rate = 200  # сколько снарядов расходуется за один выстрел
    periodicity = 500  # частота выстрелов (чем меньше значение, тем выше скорострельность)
    periodcity_time = pygame.time.get_ticks()
    image = load_image('Data/shots/04 - main - atom_gun.png')  # изображение объекта
    mask = pygame.mask.from_surface(image)  # маска объекта

    def make_shot(self, x, y):
        Shot_Atom(self, x, y)

class G05_standart_opponent(G01_standart):
    image = load_image('Data/shots/05 - vrag - standart_gun.png')  # изображение объекта
    mask = pygame.mask.from_surface(image)  # маска объекта
    type = 'shot opponent'
    speed = 5
    periodicity = 250
    damage = 1

class G06_double_opponent(G02_double):
    image = load_image('Data/shots/05 - vrag - standart_gun.png')  # изображение объекта
    mask = pygame.mask.from_surface(image)  # маска объекта
    type = 'shot opponent'
    speed = 4
    periodicity = 350
    damage = 1
    rate = 2  # сколько снарядов расходуется за один выстрел

class G061_third_opponent(G06_double_opponent):
    periodicity = 700
    speed = 4
    rate = 3  # сколько снарядов расходуется за один выстрел
    def make_shot(self, x, y):
        Shot(self, x, y - 40)
        Shot(self, x, y)
        Shot(self, x, y + 40)


class G07_fast_opponent(G03_fast):
    image = load_image('Data/shots/07 - vrag - fast_gan.png')  # изображение объекта
    mask = pygame.mask.from_surface(image)  # маска объекта
    type = 'shot opponent'

class G08_cosinus_opponent(G05_standart_opponent):
    image = load_image('Data/shots/08 - vrag - cosinus_gun.png')  # изображение объекта
    mask = pygame.mask.from_surface(image)  # маска объекта
    type = 'shot opponent'

    def make_shot(self, x, y):
        Shot_cosinus(self, x, y)

class G09_hard_opponent(G05_standart_opponent):
    image = load_image('Data/shots/09 - vrag - hurd_gun.png')  # изображение объекта
    mask = pygame.mask.from_surface(image)  # маска объекта
    type = 'shot opponent'
    periodicity = 800
    speed = 4
    rate = 1  # сколько снарядов расходуется за один выстрел
    damage = 1

    def make_shot(self, x, y):
        Shot_homing(self,x,y,glb.hero.rect.centerx, glb.hero.rect.centery, 100)


class G09_superhard_opponent(G09_hard_opponent):
    def make_shot(self, x, y):
        Shot_hard(self, self.master.rect.x+180, y-70, glb.hero.rect.centerx, glb.hero.rect.centery, 80 )
        Shot_hard(self, self.master.rect.x+510, y-100, glb.hero.rect.centerx, glb.hero.rect.centery, 80)




class G_boss_uran(G07_fast_opponent):
    periodicity = 1500
    rate = 3  # сколько снарядов расходуется за один выстрел
    name = 'boss_uran'

    def make_shot(self, x, y):
        Shot(self, x, y - 50)
        Shot(self, x, y)
        Shot(self, x, y + 50)

class G10_homing_opponent(G08_cosinus_opponent):
    def make_shot(self, x, y):
        Shot_homing(self,x,y,glb.hero.rect.centerx, glb.hero.rect.centery, 100)

class G11_boss_venera(G10_homing_opponent):
    image = load_image('Data/shots/09 - vrag - hurd_gun.png')  # изображение объекта
    mask = pygame.mask.from_surface(image)  # маска объекта
    damage = 1
    periodicity = 1000
    name = 'boss_venera'
    def make_shot(self, x, y):
        Shot_hard(self, x, y-20,glb.hero.rect.centerx, glb.hero.rect.centery-50, 250)
        Shot_homing(self,x,y,glb.hero.rect.centerx, glb.hero.rect.centery, 100)
        Shot_hard(self, x, y + 20,glb.hero.rect.centerx, glb.hero.rect.centery+50, 250)