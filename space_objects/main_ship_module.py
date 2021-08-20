from space_objects.status_health import *
from space_objects.guns import *
import myGUI
from space_objects.sounds import get_random_sound



class Main_ship(Space_Object):
    name = 'main_spaceship'  # имя
    type = 'main_spaceship'  # тип
    image = load_image('Data/main_spaceship.png')  # изображение объекта
    mask = pygame.mask.from_surface(image)  # маска объекта
    general_direction = Direction.D_RIGTH  # основное направление
    direction = Direction.D_STOP  # текущее направление
    speed = 5  # скорость движения
    health = 10  # здоровье
    max_health = health  # максимальное здоровье
    points = 0  # собранные очки
    value = 0  # сколько очков отдаст при уничтожении
    damage = 1  # какой урон наносит при столкновении
    type_explosion = 1  # уничтожение (номер анимации)
    sound_explosion = get_random_sound('Data/Sound/00_hero')  # звук при уничтожении (файл)
    protect = None

    def __init__(self, x, y, shots):
        super().__init__(allsprites_group, x, y)
        self.scale_of_XP = Scale_of_XP(self, (102,255,0) )
        self.help_shots = 1 # количество помощи по патронам
        self.help_health = 1 # количество помощи по здоровью
        self.gun = G01_standart (self, shots)  # оружие (объект)

class Protect_field(Space_Object):
    image = load_image('Data/protect.png')
    mask = pygame.mask.from_surface(image)
    font_health = pygame.font.Font('MagistralC.otf', 20)
    def __init__(self, master):
        super().__init__(allsprites_group, 0, 0)
        self.master = master
        self.name = 'protect_field'
        self.type = 'protect_field'
        self.image = self.image
        self.rect = self.image.get_rect()
        self.mask = self.mask
        self.rect.centerx = master.rect.centerx
        self.rect.centery = master.rect.centery
        self.last_rect = self.rect
        self.speed = master.speed
        self.general_direction = master.general_direction
        self.direction = Direction.D_STOP
        self.gun = None  # оружие. У оружия параметры изображение снарядов, направление, скорострельность, скорость, урон
        self.type_explosion = 2  # заменить на объект взрыва при уничтожении. Добавить объект взрыва при ранении
        self.max_health = 1
        self.health = self.max_health
        self.value = 0  # сколько очков этот объект даст при уничтожении
        self.uron = 1
        self.sound_explosion = get_random_sound('Data/Sound/01_meteorits')  # звук при уничтожении (файл)
        # self.label_health = None

    def update(self):
        super().update()
        self.rect.centerx = self.master.rect.centerx
        self.rect.centery = self.master.rect.centery
        # if self.health>1:
        #     label_health = str(self.health)
        #     self.label_health = myGUI.Text_label(label_health, self.font_health, (250, 100, 0), 50, 50)
        #     self.label_health.set_label(self.image, 45, 55)

