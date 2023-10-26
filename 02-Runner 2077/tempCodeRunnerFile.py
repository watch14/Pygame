from typing import Any
import pygame
from sys import exit

from random import randint, choice



class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1= pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
        player_walk_2= pygame.image.load('graphics/player/player_walk_2.png').convert_alpha()
        
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load('graphics/player/jump.png').convert_alpha()
        
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (130, 300))
        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound('audio/jump.mp3')
        self.jump_sound.set_volume(0.06)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300 :
            self.gravity = -11
            self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 0.3
        self.rect.y += self.gravity
        if self.rect.bottom >= 300 : self.rect.bottom = 300

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else :
            self.player_index += 0.07
            if self.player_index >= len(self.player_walk): self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]


    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()

class Obstacle(pygame.sprite.Sprite):
    def __init__ (self,type):
        super().__init__()

        if type == 'fly':
            fly_f1 = pygame.image.load('graphics/fly/fly1.png').convert_alpha()
            fly_f2 = pygame.image.load('graphics/fly/fly2.png').convert_alpha()
            self.frames = [fly_f1,fly_f2]
            y_pos = randint(120, 180)
        else :
            snail_f1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
            snail_f2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
            self.frames = [snail_f1, snail_f2]
            y_pos = 300
        
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900, 1200), y_pos))
    
    def animation_state(self):
        self.animation_index += 0.07
        if self.animation_index >= len(self.frames): self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]


    def destroy(self):
        if self.rect.x <= -100: self.kill()

    def update(self):
        self.animation_state()
        self.rect.x -=  3.75
        self.destroy()





def display_score():

    curent_time = int (pygame.time.get_ticks() / 1000) - start_time
    score_surf = font_test.render(f'{curent_time}', False, 'black')
    score_rect = score_surf.get_rect(center = (400, 30))

    screen.blit(score_surf, score_rect)
    return curent_time


def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()#reset position if game over
        return False
    else : return True

c = "font/Pixeltype.ttf"


pygame.init()

## screen display
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner 2077')     ## Game name
Clock = pygame.time.Clock()     ## Max frame rate
font_test = pygame.font.Font('font/Pixeltype.ttf', 35)    # font type and size

#music
bg_music = pygame.mixer.Sound('audio/music.wav')
bg_music.set_volume(0.03)
bg_music.play(loops = -1)

start_time = None
score = 0

## load images
sky_img = pygame.image.load('graphics/Sky.png').convert()
ground_img = pygame.image.load('graphics/ground.png').convert()
ground_rect = ground_img.get_rect(topleft = (0,300 ))
ground_rect2 = ground_img.get_rect(topleft = (785,300 ))

## Groups 
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()




##############################################################################
    # start and end screen
runner_surf = font_test.render('Runner 2077', False, 'white')
runner_surf = pygame.transform.scale_by(runner_surf, 3)
runner_rect = runner_surf.get_rect(center = (400, 70))

    #intro player image
player_stand = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_stand= pygame.transform.scale_by(player_stand, 2)
stand_rect = player_stand.get_rect(center = (400, 200))


press_surf = font_test.render('Press SPACE to Restart', False, 'white')
press_rect = press_surf.get_rect(center = (400, 330))
##############################################################################


obstacle_rect_list = []



#timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1100)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 100)



#game variable
game_active = False
new_game = True

## main 
while True:
    
    for event in pygame.event.get():
        ## Quit ##
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
      
        
            if event.type == obstacle_timer:
            #randomizer spawn snail if 0. fly if 2 
                obstacle_group.add(Obstacle(choice(['fly','snail','snail'])))
                
            
            


        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int (pygame.time.get_ticks() / 1000) 



    if game_active:
        
        ## all elaments
        screen.blit(sky_img,(0, 0))   ## img position
        screen.blit(ground_img,ground_rect)
        screen.blit(ground_img,ground_rect2)

        ## ground movement
        ground_rect.left -= 2
        ground_rect2.left -= 2

        if ground_rect.right <= 0:
            ground_rect.left = ground_rect2.right
        if ground_rect2.right <= 0:
            ground_rect2.left = ground_rect.right
    

        score = display_score()

      
        # player
        player.draw(screen)
        player.update()

        #obstacle
        obstacle_group.draw(screen)
        obstacle_group.update()

        #collisions
        game_active = collision_sprite()       


        new_game = False

      
    
    else :
        screen.fill((94, 129, 162))
        obstacle_rect_list.clear()   # clear enemies when game over
        if new_game:
            # Title Runner 2077
            screen.blit(runner_surf, runner_rect)
        else :
            ## score
            over_surf = font_test.render(f'GAME OVER : {score}', False, 'white') 
            over_surf = pygame.transform.scale_by(over_surf, 1.5)
            over_rect = over_surf.get_rect(center = (400, 70))
            screen.blit(over_surf, over_rect)
        
        #Press space
        screen.blit(press_surf, press_rect)
        screen.blit(player_stand, stand_rect)




    pygame.display.update()   ## updare every thing
    Clock.tick(120)      ## Max fps