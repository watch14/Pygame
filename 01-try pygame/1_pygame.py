import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 800))

player = pygame.Rect((450, 350, 50, 50))

run = True
while run:
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (245, 200, 66), player)

    key = pygame.key.get_pressed()
    if key[pygame.K_q] == True:
        player.move_ip(-1, 0)
    elif key[pygame.K_d] == True:
        player.move_ip(1, 0)
    elif key[pygame.K_z] == True:
        player.move_ip(0, -1)
    elif key[pygame.K_s] == True:
        player.move_ip(0, 1)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.update()

pygame.quit()