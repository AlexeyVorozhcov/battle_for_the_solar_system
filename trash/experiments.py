import pygame
import mydef
import os
from math import tan, pi, cos
import random

# p = os.path.join("C:","Users","JohnDoe","Desktop","tt.txt")
# print (p)



def rename_path(old_path):
    result_00 = old_path.split("/", maxsplit= -1)
    result = os.path.join(*result_00)
    return result


res = rename_path('Data/opponents/01_mercury/boss.png')
print(res)

#
# pygame.init()
# pygame.font.init()
# clock = pygame.time.Clock()
# fps = 60
#
# g=10
# rad = 180/pi
#
# class Flying_object(pygame.sprite.Sprite):
#     image1 = mydef.load_image('Data/shots/01 - main - standart_gun.png')
#     image2 = mydef.load_image('Data/shots/05 - vrag - standart_gun.png')
#     image3 = mydef.load_image('Data/shots/08 - vrag - cosinus_gun.png')
#
#     def __init__(self, x0, y0, tetta, v, speed ):
#         super().__init__(allsprites_group)
#         self.image = random.choice([self.image1, self.image2, self.image3,])
#         self.rect = self.image.get_rect()
#         self.x0 = x0
#         self.x = self.x0
#         self.y0 = y0
#         self.y = self.y0
#         self.tetta = tetta
#         self.v = v
#         self.tetta1 = self.tetta / rad
#         self.rect.x = self.x
#         self.rect.y = self.y
#         if self.rect.y > 600:
#             self.kill()
#         # self.time = pygame.time.get_ticks()
#         self.speed = speed
#         self.is_stop = False
#
#
#
#     def update(self):
#         if not self.is_stop:
#             self.x += self.speed
#             self.xx = self.x - self.x0
#             # self.y = self.x * tan(self.tetta1) - 1 / (2 * self.v ** 2) * (g * self.x ** 2) / (cos(self.tetta1) ** 2) + self.y0
#             self.y = self.xx * tan(self.tetta1) - ((self.xx**2)*(g/(2*self.v**2*cos(self.tetta1)**2)))
#             self.rect.x = self.x
#             print (self.tetta, self.v, self.speed)
#             print (self.y0, self.y)
#             self.rect.y = self.y0 - self.y
#             self.time = pygame.time.get_ticks()
#             # print (self.x, self.y)
#             # print (self.y0, self.y)
#             self.is_stop = mydef.random_chance([False, True], [985, 15])
#
#
# class Flying_object_2(pygame.sprite.Sprite):
#     image1 = mydef.load_image('Data/shots/01 - main - standart_gun.png')
#     image2 = mydef.load_image('Data/shots/05 - vrag - standart_gun.png')
#     image3 = mydef.load_image('Data/shots/08 - vrag - cosinus_gun.png')
#
#     def __init__(self, x0, y0, x1, y1, speed = 100 ):
#         super().__init__(allsprites_group)
#         self.image = random.choice([self.image1, self.image2, self.image3,])
#         self.rect = self.image.get_rect()
#         self.x0 = x0
#         self.y0 = y0
#         self.x1 = x1
#         self.y1 = y1
#         self.x = 0
#         self.y = 0
#         self.t = 0
#         self.step = 1 / speed
#         self.rect.x = self.x
#         self.rect.y = self.y
#         self.is_stop = False
#
#     def update(self):
#         if not self.is_stop:
#             self.t += self.step
#             if self.t > 1: self.is_stop = True
#             self.x = self.x0 + (self.x1-self.x0)*self.t
#             self.y = self.y0 + (self.y1-self.y0)*self.t
#             print((self.t, self.x, self.y))
#             self.rect.x = self.x
#             self.rect.y = self.y
#
#
#         # if not self.is_stop:
#         #     self.x += self.speed
#         #     self.xx = self.x - self.x0
#         #     # self.y = self.x * tan(self.tetta1) - 1 / (2 * self.v ** 2) * (g * self.x ** 2) / (cos(self.tetta1) ** 2) + self.y0
#         #     self.y = self.xx * tan(self.tetta1) - ((self.xx**2)*(g/(2*self.v**2*cos(self.tetta1)**2)))
#         #     self.rect.x = self.x
#         #     self.rect.y = self.y0 - self.y
#         #     self.time = pygame.time.get_ticks()
#         #     print (self.x, self.y)
#         #     self.is_stop = mydef.random_chance([False, True], [985, 15])
#
# allsprites_group = pygame.sprite.Group()
# environ['SDL_VIDEO_CENTERED'] = '1'
# screen = pygame.display.set_mode((1000,600)) # основное окно
# pygame.display.set_caption("Эксперимент")
# time = pygame.time.get_ticks()
# # Flying_object_2(100,100, 500,500, 50)
# # Главный цикл программы
# while True:
#     if mydef.check_timer(time, 100):
#         Flying_object(500, 300, random.randint(10,80), random.randint(30,100), 3)
#         Flying_object(500, 300, random.randint(280, 350), random.randint(30, 100), -3)
#         Flying_object(500, 300, random.randint(100, 170), random.randint(30, 100), 3)
#         Flying_object(500, 300, random.randint(190, 260), random.randint(30, 100), -3)
#         # Flying_object_2(100,300, 500, random.randint(100,500), 50)
#         time = pygame.time.get_ticks()
#     events = pygame.event.get()
#     # действия игрока
#     for event in events:
#         if event.type == pygame.QUIT:
#             mydef.terminate()
#
#     screen.fill((0, 0, 0))
#     allsprites_group.update()
#     allsprites_group.draw(screen)
#     pygame.display.flip()
#     clock.tick(fps)
#
# # # задаёмся переменными
# # x = 100  # координата х
# # tetta = 30  # начальный угол
# # g = 9.81  # ускорение свободного падения (м/с**2), можно подставить значение и для Луны
# # v = 1020  # начальная скорость (м/с), типовая скорость снаряда
# # y0 = 2  # начальная вертикальная координата
# #
# # # сразу задаёмся радианами
# # rad = 180 / pi
# tetta1 = tetta / rad  # вместо градусов получили количество радиан