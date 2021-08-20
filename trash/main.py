import os
import pygame
import vars
import main_menu
import levels
import main_game

# инициализация экрана
os.environ['SDL_VIDEO_CENTERED'] = '1'
vars.screen = pygame.display.set_mode(vars.SIZE) # основное окно
pygame.display.set_caption("Моя вторая игра на Python. Ворожцов А.В.")

is_run = True
while is_run:
    # главное меню, возвращает номер выбранного уровня
    vars.select_level = main_menu.start_main_menu()
    print('Выбранный уровень: ', vars.select_level)

    # получаем структуру выбранного уровня
    level_structure = levels.load_level(vars.select_level)
    print (level_structure)

    #запускаем основную игру, передаем в нее структуру
    main_game.start_main_game(level_structure)