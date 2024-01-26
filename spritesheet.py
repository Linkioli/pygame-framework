import pygame

class SpriteSheet():
    def __init__(self, image, size=(16, 16), colorkey=(255, 0, 255)):
        self.sheet = image
        self.size = size
        self.colorkey = colorkey
        self.framecount = self.sheet.get_width() // self.size[0]


    def get_frame(self, frame):
        surf = pygame.Surface(self.size).convert_alpha()
        surf.fill(self.colorkey)
        surf.blit(self.sheet, (0, 0), ((frame * self.size[0]), 0, self.size[0], self.size[1]))
        surf.set_colorkey(self.colorkey)
        return surf


    def get_frames(self, frame_list=[]):
        frames = []
        if len(frame_list) == 0:
            for frame in range(self.framecount):
                frames.append(self.get_frame(frame))
            return frames

        for frame in frame_list:
            frames.append(self.get_frame(frame))
        return frames
