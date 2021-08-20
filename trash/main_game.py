import pygame
import vars
import mydef
import levels
import game_objects
import myGUI

class Game():
    bg = None
    level_structure = None
    main_ship = None

class Background(pygame.sprite.Sprite):
    def __init__(self, image, posx=0, speed=50):
        super().__init__(vars.bg_group)
        self.traversed = 0
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.w = self.image.get_width()
        self.posx = posx
        self.speed = speed
        self.time = pygame.time.get_ticks()
        self.abroad = vars.Gameboard.w - self.w
        self.is_shaking = False
        self.time_shaking = pygame.time.get_ticks()
        self.counter_shaking =0

    def update(self, *args):
        if self.is_shaking and not mydef.check_timer(self.time_shaking, 800) :
            if self.counter_shaking>=0 and self.counter_shaking<=3:
                self.rect = self.rect.move(2,0)
            if self.counter_shaking >= 4 and self.counter_shaking <= 7:
                self.rect = self.rect.move(-2,0)
            if self.counter_shaking ==7:
                self.counter_shaking = 0
            self.counter_shaking +=1
        else:
            self.is_shaking = False
            self.counter_shaking =0
            if mydef.check_timer(self.time, self.speed):
                self.rect = self.rect.move(-1,0)
                self.time = pygame.time.get_ticks()
                self.traversed +=1
        # if self.posx <= self.abroad:
        #     vars.screen.blit(self.image, (self.posx + self.w   , 0))
        # if abs(self.posx) >= self.w:
        #     self.posx = 0

def make_sprite(n):
    if Game.level_structure.get(Game.bg.traversed) != None:
        obj = Game.level_structure[Game.bg.traversed][0]
        pos_y = Game.level_structure[Game.bg.traversed][1]
        temp = Game.level_structure.pop(Game.bg.traversed)
        obj(vars.gameboard, vars.allsprites_group, x=vars.gameboard.w, y=pos_y)


def check_of_gameover():
    if len(vars.allsprites_group) == 3 and Game.main_ship.protect != None and len(Game.level_structure) == 0:
        Game.main_ship.protect.kill()
    if len(Game.level_structure) == 0 and len(vars.allsprites_group) == 2:
        print("LEVEL COMPLETE")
        #Level_comlete.level_comlpete()

def init_level(level_structure_):
    vars.running_game = True
    vars.allsprites_group.empty()
    vars.explosion_group.empty()
    Game.bg = Background(levels.get_image_background(vars.select_level))
    Game.level_structure = level_structure_
    Game.main_ship =  game_objects.Main_ship(vars.gameboard, vars.allsprites_group, x=30, y=150)

def start_main_game(level_structure_):
    init_level(level_structure_)
    while vars.running_game:
        events = pygame.event.get()
        # действия игрока
        for event in events:
            if event.type == pygame.QUIT:
                mydef.terminate()
            if event.type == pygame.KEYUP and event.key != pygame.K_SPACE:
                Game.main_ship.direction = game_objects.Direction.D_STOP
            if event.type == pygame.KEYDOWN and event.key == pygame.K_0:
                pass
                # для тестов
                #main_ship.protect = game_objects.Protect_field(main_ship, gameboard, allsprites_group)
                # game_objects.Bonus_protect(gameboard,allsprites_group, x=500, y=300)
                # game_objects.Big_ship(gameboard, allsprites_group, x=900, y=300)
                #Level_comlete.level_comlpete()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE :
                pass
                #pause()
        Game.main_ship.gun.is_shot = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            Game.main_ship.direction = game_objects.Direction.D_RIGTH
        if keys[pygame.K_LEFT]:
            Game.main_ship.direction = game_objects.Direction.D_LEFT
        if keys[pygame.K_DOWN]:
            Game.main_ship.direction = game_objects.Direction.D_DOWN
        if keys[pygame.K_UP]:
            Game.main_ship.direction = game_objects.Direction.D_UP
        if keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
            Game.main_ship.direction = game_objects.Direction.D_RIGTH_DOWN
        if keys[pygame.K_RIGHT] and keys[pygame.K_UP]:
            Game.main_ship.direction = game_objects.Direction.D_RIGTH_UP
        if keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
            Game.main_ship.direction = game_objects.Direction.D_LEFT_DOWN
        if keys[pygame.K_LEFT] and keys[pygame.K_UP]:
            Game.main_ship.direction = game_objects.Direction.D_LEFT_UP
        if keys[pygame.K_SPACE]:
            Game.main_ship.gun.is_shot = True


        make_sprite(Game.bg.traversed)
        vars.screen.fill((0, 0, 0))
        vars.bg_group.update()
        vars.bg_group.draw(vars.screen)
        vars.allsprites_group.update()
        vars.allsprites_group.draw(vars.screen)
        vars.explosion_group.update()
        vars.explosion_group.draw(vars.screen)
        #to_check_on_collide(allsprites_group)
        vars.statusboard.surf.fill((0,0,0))
        shots_label = myGUI.Text_label('Снаряды: '+ str(Game.main_ship.gun.shots), vars.font_label_shots, (255,255,255), vars.statusboard.w-5, 30)
        shots_label.set_label(vars.statusboard.surf,0,10)
        points_label = myGUI.Text_label('Очки: ' + str(Game.main_ship.points), vars.font_label_shots, (255, 255, 255),
                                       vars.statusboard.w - 5, 30)
        points_label.set_label(vars.statusboard.surf, 0, 40)
        vars.screen.blit(vars.statusboard.surf, (vars.gameboard.w, 0))

        pygame.display.flip()
        vars.clock.tick(vars.FPS)