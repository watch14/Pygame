import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join

pygame.init()

pygame.display.set_caption("Ninja Frog V") #caption

BG_COLOR = (87, 25, 35)
WIDTH, HEIGHT  = 1000, 800  #screen width an d height
FPS = 60
PLAYER_VEL = 5     # player mevement speed

window = pygame.display.set_mode((WIDTH, HEIGHT))

def main(window):
    run = True
    while True:
        Clock.tick(FPS)

if __name__ == "__main__":
    main(window)