from space_objects.base import *


class Scale_of_XP(pygame.sprite.Sprite):
    def __init__(self, obj, color):
        super().__init__(allsprites_group)
        self.name = None
        self.type = None
        self.obj = obj
        self.color = color
        self.d = obj.rect.width - 1
        self.p = self.d / obj.max_health
        self.image = pygame.Surface((self.d, 5))
        pygame.draw.rect(self.image, color, (0, 0, self.d, 4), 1)
        pygame.draw.rect(self.image, color, (0, 0, int(self.p * obj.health), 4), 0)
        self.rect = self.image.get_rect()
        self.rect.x = obj.rect.x
        self.rect.y = obj.rect.y-5

    def update(self):
        if self.obj.health<=0:
            self.kill()
        self.p = self.d / self.obj.max_health
        self.image = pygame.Surface((self.d, 5))
        pygame.draw.rect(self.image, self.color, (0, 0, self.d, 4), 1)
        pygame.draw.rect(self.image, self.color, (0, 0, int(self.p * self.obj.health), 4), 0)
        self.rect.x = self.obj.rect.x
        self.rect.y = self.obj.rect.y-5