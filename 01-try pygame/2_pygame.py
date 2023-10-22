import pygame
from pygame.locals import *

pygame.init()

sc_width = 1000
sc_height = 800

screen = pygame.display.set_mode((sc_width, sc_height))
pygame.display.set_caption("Do it!")

#define game variable
tile_size = 50
#########################################################


# Load the background image
bg_img = pygame.image.load('img/Background/Brown.png')
bg_width = bg_img.get_width()
bg_height = bg_img.get_height()
#################################################################


#show grid 
def draw_grid():
	for line in range(0, 20):
		pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (sc_width, line * tile_size))
		pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, sc_height))
#####################################################################

class player():
     def __init__(self, x, y):
          img = pygame.image.load('')


class World():
    def __init__(self, data):
        self.tile_list = []
        #load image
        box_img = pygame.image.load('img/Background/Gray.png')
        grass_img = pygame.image.load('img/Background/Green.png')
        
        row_count = 0
        
        for row in data:
            collum_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(box_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = collum_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                
                if tile == 2:
                    img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = collum_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                collum_count += 1
            row_count += 1
    def draw(self):
         for tile in self.tile_list:
              screen.blit(tile[0], tile[1])
                      

world_data = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
]



world = World(world_data)  

run = True
while run:

    #Background image
    for x in range(0, sc_width, bg_width):
        for y in range(0, sc_height, bg_height):
            screen.blit(bg_img, (x, y))
   
    world.draw()

    draw_grid()


    #exit / quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



    pygame.display.update()

pygame.quit()
