import glb
import public_vars
from space_objects.my import *
from space_objects.sounds import *
from space_objects.explosion import *
from mydef import random_chance




pygame.mixer.init()



class Direction():
    D_RIGTH = [1, 0]
    D_DOWN = [0, 1]
    D_LEFT = [-1, 0]
    D_UP = [0, -1]
    D_STOP = [0, 0]
    D_RIGTH_DOWN = [1, 1]
    D_LEFT_DOWN = [-1, 1]
    D_RIGTH_UP = [1, -1]
    D_LEFT_UP = [-1, -1]

class Space_Object(pygame.sprite.Sprite):
    name = None  # имя
    type = None  # тип
    image = load_image("Data/main_spaceship.png", 0, 0) # изображение объекта
    mask = pygame.mask.from_surface(image) # маска объекта
    general_direction = None  # основное направление
    direction = None  # текущее направление
    speed = None  # скорость движения
    health = None  # здоровье
    max_health = health  # максимальное здоровье
    points = 0  # собранные очки
    value = 0  # сколько очков отдаст при уничтожении
    damage = 0 # какой урон наносит при столкновении
    type_explosion = 0  # уничтожение (номер анимации)
    sound_explosion = None  # звук при уничтожении (файл)
    is_couse_shaking = False # вызывает тряску экрана при уничтожении
    is_couse_trophy = 0 # вероятность выдачи трофея после смерти
    is_boss = False # это босс
    is_may_abroad = False # может выходить за границы экрана

    def __init__(self, group, x, y):
        super().__init__(group)
        self.num_step = 0  # номер хода
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.last_rect = self.rect
        self.status_health = None  # полоска здоровья (объект)
        self.gun = None  # оружие (объект)

    # проверка выхода объекта за экран
    def check_out_screen(self):
        if self.type != "protect_field" and not self.is_may_abroad:
            out_up = self.rect.y < 0
            out_down = self.rect.bottom > HEIGHT_GAMEBOARD
            if self.name == 'mer_03_alien' or self.name == 'mer_01':
                out_down = self.rect.bottom > HEIGHT_GAMEBOARD + 50
            if self.type == 'main_spaceship':
                out_left = self.rect.left < 0
                out_right = self.rect.right > WIDTH_GAMEBOARD
                if out_right or out_down or out_left or out_up:
                    self.rect = self.last_rect
            else:
                out_left = self.rect.right < 0 - 50
                out_right = self.rect.left > WIDTH_GAMEBOARD + 50
                if out_right or out_down or out_left or out_up:
                    if self.status_health!=None:
                        self.status_health.kill()
                    self.kill()

    # движение
    def to_move(self):
        self.last_rect = self.rect
        self.rect = self.rect.move(self.direction[0] * self.speed, self.direction[1] * self.speed)
        self.num_step += 1
        # проверяем выход за границы
        self.check_out_screen()


    # получить урон
    def to_destruction(self, uron=1):
        return_points = 0
        self.health -= uron
        if self.health <=0:
            if self.sound_explosion!=None:
                self.sound_explosion.play()
            if self.is_couse_shaking:
                glb.background.is_shaking = True
                glb.background.time_shaking = pygame.time.get_ticks()
            Explosion(self, is_kill=True)
            return_points = self.value
            if self.type == 'bonus' or self.type == 'bonus_crystall':
                glb.make_fly_bonus(self)
            if self.is_couse_trophy>0:
                glb.make_trophy(self)
            self.kill()

        else:
            Explosion(self, is_kill=False)

        return return_points

    def ai_control(self):
        if self.type == "opponent":
            if self.gun!=None and self.gun.shots>0:
                self.gun.is_shooting =random_chance([True,False],[10,90])
                # if random_chance([True,False],[15,85]):
                #     self.gun.is_shooting = not self.gun.is_shooting



    def update(self):
        self.to_move()
        if self.gun != None:
            self.gun.to_shoot()
            self.ai_control()