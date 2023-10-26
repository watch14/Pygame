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

################################################# player
#player calss
class Player(pygame.sprite.Sprite):
    COLOR = (255, 0, 0)
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y ,width, height)
        self.x_vel = 0     # movement
        self.y_vel = 0     # jump
        self.mask = 0
        self.direction = "left"
        self.animation_count = 0
    
    def move(self , dx, dy):  
        self.rect.x += dx   # left / right
        self.rect.y += dy   # up / donw

    def move_right(self, vel):       # move right
        self.x_vel = vel
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0

    def move_left(self, vel):       # move left
        self.x_vel = -vel
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0

    def loop(self, fps):
        self.move(self.x_vel, self.y_vel)

    def loop(self, fps):
        self.move(self.x_vel, self.y_vel)

#player movement
def handle_move(player):
    keys = pygame.key.get_pressed()
    
    player.x_vel = 0

    if keys[pygame.K_LEFT]:   #left key
        player.move_left(PLAYER_VEL)
    if keys[pygame.K_RIGHT]:   #right key
        player.move_right(PLAYER_VEL)

################################################# player


################# background
def get_background(name):
    ##image = pygame.image.load(join("img", "bg", name))  # load image
    
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current script
    image_path = os.path.join(script_dir, "img", "bg", name)  # Construct the absolute path to the image
    image = pygame.image.load(image_path)  # Load the image

    _, _, width, height = image.get_rect()    # x, y, width, height = make rectagle
    tiles = []

    for i in range(WIDTH // width + 1):    # number of tiles + 1 to make shure no gap
        for j in range(HEIGHT // height + 1):
            pos = (i * width , j * height)  ## position for every tile to fill screen
            tiles.append(pos)

    return tiles, image

################# background


##################################### draw

def draw(window, background, bg_image, player):
    for tile in background:
        window.blit(bg_image, tile)    # display background in screen

    player.draw(window)   # draw player
    pygame.display.update()

##################################### draw




######################################## main function

def main(window):
    Clock = pygame.time.Clock()   # lock fps
    background, bg_image= get_background("Yellow.png")

    player = Player(100, 100, 50, 50)

    run = True
    while run:
        Clock.tick(FPS)   # max fps

        for event in pygame.event.get():
            if event.type == pygame.QUIT:    # EXIT game
                run = False
                break   # or exit()
        
        player.loop(FPS)
        handle_move(player)
        draw(window, background, bg_image, player)

    pygame.QUIT()
    quit()

######################################## end main function

############################# run code 

if __name__ == "__main__":
    main(window)

############################# run code 
