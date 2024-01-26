import pygame
from settings import *
from framework.spritesheet import *
from framework.animation import *

class Tile:
    def __init__(self, level, pos, image):
        self.pos = list(pos)
        self.spritesheet = SpriteSheet(image, (TILESIZE, TILESIZE))
        self.image = self.spritesheet.get_frame(0)
        self.rect = self.image.get_rect(topleft = self.pos)
        self.level = level
        self.type = "tile"


    def update(self, surf, offset=(0, 0)):
        self.rect.topleft = self.pos
        self.render(surf, offset)

    
    def render(self, surf, offset):
        surf.blit(self.image, ((self.pos[0] - offset[0]), (self.pos[1] - offset[1])))

class AnimatedTile(Tile):
    def __init__(self, level, pos, image, dur=10, loop=True):
        super().__init__(level, pos, image)
        self.animation = Animation(self.spritesheet.get_frames(), dur, loop=loop)

    def update(self, surf, offset=(0, 0)):
        super().update(surf, offset)
        self.animation.update()

    def render(self, surf, offset):
        self.image = self.animation.img()
        super().render(surf, offset)
