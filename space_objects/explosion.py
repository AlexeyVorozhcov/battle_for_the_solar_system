from math import tan, pi, cos
import pygame
from space_objects.my import *
from public_vars import *
import random
import glb





class Explosion(pygame.sprite.Sprite):
    TYPES = {
        0: get_load_images('Data/destruction_00', ".png", 0, 0),
        1: get_load_images('Data/destruction_01', ".png", 0, 0),
        2: get_load_images('Data/destruction_02', ".png", 0, 0),
        3: get_load_images('Data/destruction_03', ".png", 0, 0),
        4: get_load_images('Data/destruction_04', ".png", 0, 0),
        5: get_load_images('Data/destruction_05', ".png", -4, -4),
        6: get_load_images('Data/destruction_06', ".png", 800, 800),
        7: get_load_images('Data/destruction_07', ".png", 546, 618)
    }

    def __init__(self, obj, is_kill): # isKill True - полный взрыв, False - частичный, ранение
        group = explosion_group
        self.type = 'explosion'
        if obj.type_explosion==7:
            # group=allsprites_group
            self.type = 'atom_shot'
            self.name = 'atom_shot'
            self.master = glb.hero.gun
            self.damage = 10
            self.health = 100
        super().__init__(group)
        self.frames = Explosion.TYPES[obj.type_explosion] #набор кадров
        self.num_frame = -1 # текущий номер кадра
        self.image = self.frames[self.num_frame] # текущий кадр
        self.rect = self.image.get_rect()
        self.rect.centerx = obj.rect.centerx
        self.rect.centery = obj.rect.centery
        self.is_kill = is_kill

    def update(self):
        self.num_frame = (self.num_frame + 1)
        duration = 0 # продолжительность взрыва в кадрах
        if self.is_kill:
            duration = len(self.frames)
        if not self.is_kill and len(self.frames)>3:
            duration = 3
        if self.num_frame>= duration:
            self.kill()
        else:
            self.image = self.frames[self.num_frame] # текущий кадр

    def to_destruction(self, f):
        pass


# class Atom_Explosion(Explosion):
#
#     def __init__(self, obj, is_kill):
#         super().__init__(obj, is_kill)
#         self.type = 'main_spaceship'
#         self.name = 'atom_gun'
#
#         allsprites_group.add(self)