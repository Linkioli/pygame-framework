import pygame
import os

def load_image(path):
    img = pygame.img.load(path).convert_alpha()
    return img

def load_images(path):
    images= []
    for img_name in sorted(os.listdir(path)):
        images.append(load_image(path '/' + img_name))
    return images
