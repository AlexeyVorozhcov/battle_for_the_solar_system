import pygame
from space_objects.base import *
import random
import mydef

pygame.mixer.init()

def get_sound_pack(path, end_switch=".wav"):
    result = []
    try:
        files = mydef.get_list_files(path, end_switch)
        fullpaths = []
        for f in files:
            fullpaths.append(path + '/' + f)
        for sound in fullpaths:
            result.append(pygame.mixer.Sound(sound))
    except Exception:
        print("Ошибка со звуком get_sound_pack. Нажмите Enter...")
        input()
    return result


sounds_packs = {
    'Data/Sound/00_hero': get_sound_pack('Data/Sound/00_hero'),
    'Data/Sound/01_meteorits': get_sound_pack('Data/Sound/01_meteorits'),
    'Data/Sound/02_bobms': get_sound_pack('Data/Sound/02_bobms'),
    'Data/Sound/03_standart_opponents': get_sound_pack('Data/Sound/03_standart_opponents')

}

def get_random_sound(path, end_switch='.wav'):
    result = None
    try:
        files = mydef.get_list_files(path, end_switch)
        fullpath=[]
        for f in files:
            fullpath.append(path+ '/' + f)
        result = pygame.mixer.Sound(random.choice(fullpath))
    except Exception:
        print("Ошибка со звуком get_random_sound. Нажмите Enter...")
        input()
    return result

def get_random_file(path, end_switch='.mp3'):
    result = None
    try:
        files = mydef.get_list_files(path, end_switch)
        fullpath = []
        for f in files:
            fullpath.append(path + '/' + f)
        result = random.choice(fullpath)
    except Exception:
        print("Ошибка со звуком get_random_file. Нажмите Enter...")
        input()
    return result

def play_fone_music(path, volume=0.5):
    try:
        pygame.mixer.music.load(get_random_file(path))
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(-1)
    except Exception:
        print("Ошибка со звуком play_fone_music. Нажмите Enter...")
        input()

def stop_fone_music():
    pygame.mixer.music.stop()

def pause_fone_music():
    pygame.mixer.music.pause()

def unpouse_fone_music():
    pygame.mixer.music.unpause()