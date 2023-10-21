import pygame
from sys import exit
from random import randint

def display_score():

    curent_time = int (pygame.time.get_ticks() / 1000) - start_time
    score_surf = font_test.render(f'{curent_time}', False, 'black')
    score_rect = score_surf.get_rect(center = (400, 30))

    screen.blit(score_surf, score_rect)
    return curent_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 3.75

            if obstacle_rect.bottom == 300: screen.blit(snail_img, obstacle_rect)
            else : screen.blit(fly_img , obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        
        return obstacle_list
    else : return []

def collisions(player, obstacles):
    if obstacles:
        for obstacles_rect in obstacles:
            if player.colliderect(obstacles_rect): return False
    return True



pygame.init()

start_time = None
score = 0


## screen display
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner 2077')     ## Game name
Clock = pygame.time.Clock()     ## Max frame rate
font_test = pygame.font.Font('font/Pixeltype.ttf', 35)    # font type and size


## load images
sky_img = pygame.image.load('graphics/Sky.png').convert()
ground_img = pygame.image.load('graphics/ground.png').convert()

# text
# score_surf = font_test.render('Runner 2077', False, 'black')
# score_rect = score_surf.get_rect(center = (400, 30)) 



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


## obstacles
# snail
snail_img = pygame.image.load('graphics/snail/snail1.png').convert_alpha()  
#fly
fly_img = pygame.image.load('graphics/fly/fly1.png').convert_alpha()

obstacle_rect_list = []


#player
player_img = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_img.get_rect(midbottom = (130, 300))
player_gravity = 0


#timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 900)

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

            #jump mouse    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos):
                    if player_rect.bottom >= 300: player_gravity = -20
            #jump space    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: 
                        if player_rect.bottom >= 300: player_gravity = -11
        
            if event.type == obstacle_timer:
            #randomizer spawn snail if 0. fly if 2 
                if randint(0, 2):
                    obstacle_rect_list.append(snail_img.get_rect(midbottom = (randint(900, 1100), 300)))
                else:
                    obstacle_rect_list.append(fly_img.get_rect(midbottom = (randint(900, 1100), randint(120, 180))))
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int (pygame.time.get_ticks() / 1000) 


    if game_active:
        ## all elaments
        screen.blit(sky_img,(0, 0))   ## img position
        screen.blit(ground_img,(0, 300))
        # pygame.draw.rect(screen,'orange', score_rect,0, 5)  # draw
        # screen.blit(score_surf, score_rect)

        score = display_score()

        # # snail / movement
        # snail_rect.x -= 3.5
        # if snail_rect.right < 0: snail_rect.left = 850
        # screen.blit(snail_img, snail_rect)

        # player / jump
        player_gravity += 0.35
        player_rect.y += player_gravity 
        if player_rect.bottom >= 300: player_rect.bottom = 300
        screen.blit(player_img, player_rect)
        
        #obstacle movement
        obstacle_rect_list =  obstacle_movement(obstacle_rect_list)
        
        #collisions
        game_active = collisions(player_rect, obstacle_rect_list)


        new_game = False


        
    
    else :
        screen.fill((94, 129, 162))
        obstacle_rect_list.clear()
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