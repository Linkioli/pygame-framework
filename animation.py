import pygame

class Animation:
    def __init__(self, images, image_dur=10, loop=True):
        self.images = images
        self.length = len(self.images)
        self.loop = loop
        self.image_duration = image_dur
        self.done = False
        self.frame = 0

    def copy(self):
        return Animation(self.images, self.image_duration, self.loop)

    def update(self):
        if self.loop:
            self.frame = (self.frame + 1) % (self.image_duration * len(self.images))
        else:
            self.frame = min(self.frame + 1, self.image_duration * len(self.images) - 1)
            if self.frame == self.image_duration * len(self.images) - 1:
                self.done = True

    def img(self):
        return self.images[int(self.frame / self.image_duration)]
