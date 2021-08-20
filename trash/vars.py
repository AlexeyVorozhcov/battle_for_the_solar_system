import pygame
import os

# для использования общих переменных и констант

pygame.init()
pygame.font.init()

FPS = 60
clock = pygame.time.Clock()
select_level = None # выбранный текущий уровень


# основное игровое поле
class Gameboard():
    w, h = 1000, 600
    rect = pygame.Rect((0, 0), (w, h))  # виртуальная область игрового поля
    surf = pygame.Surface((w, h))

# боковое поле
class Statusboard():
    w, h = 250, Gameboard.h
    rect = pygame.Rect(Gameboard.rect.topright, (w, h))  # виртуальная область статус-поля
    surf = pygame.Surface((w,h))
    pygame.draw.rect(surf, (100,100,100), (1,1,w-1,h-1),2)

SIZE = (Gameboard.w + Statusboard.w, Gameboard.h) # размер окна
screen = None

gameboard = Gameboard()
statusboard = Statusboard()
font_label_shots = pygame.font.Font(None, 30)
bg_group = pygame.sprite.Group()
labelsprites_group = pygame.sprite.Group()

running_game = True
allsprites_group = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()