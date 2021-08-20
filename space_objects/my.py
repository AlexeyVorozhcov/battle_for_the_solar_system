import pygame
from os import listdir

def check_timer (start_time, action_time):
    if pygame.time.get_ticks()-start_time >= action_time: return True
    else: return False

'''Получить список файлов в директории
dir - относительный путь
end_switch  - фильтр по расширению'''


def get_list_files(dir, end_switch):
    files = [f for f in listdir(dir) if f.endswith(end_switch)]
    return files


''' Получить изображение из файла
name - имя файла
w, h - параметры изменения изображения. 
Значения Больше нуля - установить указанные размеры. 
Значения меньше нуля - изменить размеры изображения в указанное количество раз'''


def load_image(name, w=0, h=0):
    fullname = name
    image = pygame.image.load(fullname).convert_alpha()
    try:
        if name[-2:] == "jpg":
            image = pygame.image.load(fullname).convert()
        else:
            image = pygame.image.load(fullname).convert_alpha()
    except:
        print('Cannot load image: ', name)
        print(Exception)
        #raise SystemExit()

    if w > 0 and h > 0:
        image_result = pygame.transform.scale(image, (w, h))  # устанавливаем заданный размер
    elif w < 0 and h < 0:
        image_result = pygame.transform.scale(image, (
            image.get_width() // (-w), image.get_height() // (-h)))  # уменьшаем в w раз
    else:
        image_result = image
    print("Загрузка " + fullname)
    return image_result


''' Загрузка в список изображений: директория, расширение, 
параметры изменения изображения (см. load_image)'''


def get_load_images(directory, end_switch, w, h):
    files = get_list_files(directory, end_switch)
    result = []
    for f in files:
        fullname = directory + '/' + f
        result.append(load_image(fullname, w, h))
    return result

def get_mask_from_list_of_images(images):
    masks = []
    for image in images:
        masks.append(pygame.mask.from_surface(image))
    return masks
