import pygame
import game_objects
import mydef

class Standart_gun_main_01(game_objects.Space_Object):
    name = 'standart_gun'
    type = 'shot_main'
    image= mydef.load_image('Data/shots/01 - main - standart_gun.png')
    mask = pygame.mask.from_surface(image)
    speed = 12
    general_direction = game_objects.Direction.D_RIGTH
    direction = game_objects.Direction.D_RIGTH
    periodicity = 60
    uron = 1
    periodcity_time = pygame.time.get_ticks()
    shots = 500
    type_explosion = 0
    max_health = 1
    health = max_health
    value = 0  # сколько очков этот объект даст при уничтожении
    points = 0
    is_shot = False

    def __init__(self,gameboard, group, x, y):
        super().__init__(gameboard, group)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.last_rect = self.rect



