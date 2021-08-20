import space_objects.opponents_mercury
import space_objects.opponents_venera
import space_objects.opponents
import space_objects.opponents_02
import space_objects.bombs_meteorits
import space_objects.bonuses
from space_objects.guns import *
from mydef import load_image
import random

b_pack = [space_objects.bombs_meteorits.Meteorit_01,
          space_objects.bombs_meteorits.Meteorit_02,
          space_objects.bombs_meteorits.Bomb_01,
          space_objects.bombs_meteorits.Bomb_02,
          space_objects.bonuses.Bonus_shot,
          space_objects.bonuses.Bonus_shot_double,
          space_objects.bonuses.Bonus_shot_fast,
          space_objects.bonuses.Bonus_health,
          space_objects.bonuses.Bonus_protect,
          space_objects.bonuses.Bonus_crystall_big,
          space_objects.bonuses.Bonus_crystall_small
          ]
class OP_Sun_Uran(space_objects.opponents.OP_boss_uran2):
    def kill(self):
        OP_Sun_Saturn(WIDTH_GAMEBOARD-1,250)
        play_fone_music('Data/Sound/fon_boss', 1)  # включаем фоновую музыку
        super().kill()
    def ai_control(self):
        super().ai_control()
        if random_chance([True, False], [2, 99]):
            random.choice(b_pack)(WIDTH_GAMEBOARD-1, random.randint(1, HEIGHT_GAMEBOARD-1))

class OP_Sun_Saturn(space_objects.bombs_meteorits.Boss_Saturn):
    def kill(self):
        OP_Sun_Upiter(WIDTH_GAMEBOARD - 1, 350)
        play_fone_music('Data/Sound/fon_boss', 1)  # включаем фоновую музыку
        super().kill()
    def ai_control(self):
        super().ai_control()
        if random_chance([True, False], [2, 99]):
            random.choice(b_pack)(WIDTH_GAMEBOARD-1, random.randint(1, HEIGHT_GAMEBOARD-1))

class OP_Sun_Upiter(space_objects.opponents.OP_Boss_upiter):
    def kill(self):
        OP_Sun_Mars(WIDTH_GAMEBOARD - 1, 350)
        play_fone_music('Data/Sound/fon_boss', 1)  # включаем фоновую музыку
        super().kill()

    def ai_control(self):
        super().ai_control()
        if random_chance([True, False], [2, 99]):
            random.choice(b_pack)(WIDTH_GAMEBOARD - 1, random.randint(1, HEIGHT_GAMEBOARD - 1))

class OP_Sun_Mars(space_objects.opponents_02.OP_06_Boss_mars):
    def kill(self):
        s = OP_Sun_Earth1(WIDTH_GAMEBOARD - 1, 150)
        s.is_make_boss2 = True
        play_fone_music('Data/Sound/fon_boss', 1)  # включаем фоновую музыку
        super().kill()
    def ai_control(self):
        super().ai_control()
        if random_chance([True, False], [2, 99]):
            random.choice(b_pack)(WIDTH_GAMEBOARD-1, random.randint(1, HEIGHT_GAMEBOARD-1))

class OP_Sun_Earth1(space_objects.opponents_02.OP_boss1_Earth):
    def kill(self):
        OP_Sun_Earth2(WIDTH_GAMEBOARD - 1, 250)
        play_fone_music('Data/Sound/fon_boss', 1)  # включаем фоновую музыку
        super().kill()
    def ai_control(self):
        super().ai_control()
        if random_chance([True, False], [2, 99]):
            random.choice(b_pack)(WIDTH_GAMEBOARD-1, random.randint(1, HEIGHT_GAMEBOARD-1))

class OP_Sun_Earth2(space_objects.opponents_02.OP_boss2_Earth):
    def kill(self):
        OP_Sun_Venera(WIDTH_GAMEBOARD - 1, 350)
        play_fone_music('Data/Sound/fon_boss', 1)  # включаем фоновую музыку
        super().kill()
    def ai_control(self):
        super().ai_control()
        if random_chance([True, False], [2, 99]):
            random.choice(b_pack)(WIDTH_GAMEBOARD-1, random.randint(1, HEIGHT_GAMEBOARD-1))

class OP_Sun_Venera(space_objects.opponents_venera.OP_boss_Venera):
    def kill(self):
        OP_Sun_Merc(WIDTH_GAMEBOARD - 1, 150)
        play_fone_music('Data/Sound/fon_boss', 1)  # включаем фоновую музыку
        super().kill()
    def ai_control(self):
        super().ai_control()
        if random_chance([True, False], [2, 99]):
            random.choice(b_pack)(WIDTH_GAMEBOARD-1, random.randint(1, HEIGHT_GAMEBOARD-1))

class OP_Sun_Merc(space_objects.opponents_mercury.OP_Boss_merc):
    def kill(self):
        super().kill()
    def ai_control(self):
        super().ai_control()
        if random_chance([True, False], [2, 99]):
            random.choice(b_pack)(WIDTH_GAMEBOARD-1, random.randint(1, HEIGHT_GAMEBOARD-1))