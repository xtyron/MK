import pygame

import json
from player import Player

x = 0
y = 0


player_img = pygame.image.load("res/player_forward_movement_1.PNG")

pygame.init()


player = Player("Masha", 100, 12)

clock = pygame.time.Clock()
map_list = [[1,1,1,1,1,1,1],
            [2,2,2,2,2,2,1],
            [3,3,3,3,3,3,1],
            [4,4,4,4,4,4,1],
            [5,5,5,5,5,5,1],
            [6,6,6,6,6,6,1],
            [6,6,6,6,6,6,1],
            [6,6,6,6,6,6,1]
            ]
with open("Cozy Garten\startingmap.json", "w") as f:
     json.dump(map_list, f)

rechtange_size = 32
rechtange_amount = len(map_list)


screen_height = rechtange_size * rechtange_amount
screen_width = rechtange_size * rechtange_amount

scale = 32

screen = pygame.display.set_mode((screen_height, screen_width))
pygame.display.set_caption("Cozy Garden")

running = True



font = pygame.font.SysFont(None, 30)

for i in range(len(map_list)):
    x = 0
    if i != 0:
        y += rechtange_size
    for j in range(len(map_list[i])):
            if map_list[i][j] == 1:
                 
                pygame.draw.rect(screen,(0,250,0),(x, y, rechtange_size, rechtange_size))
                pygame.draw.rect(screen,(0,0,0), (x+1, y+1, rechtange_size - 2, rechtange_size - 2))
            x += rechtange_size


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    coordinates_in_str = "x: " + str(player.x) + " y: " + str(player.y)

    screen.fill((0,0,0))

    text = font.render(coordinates_in_str, True, (255, 255, 255))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
         player.y -= player.movement_speed
         print("up")
    if keys[pygame.K_s]:
         player.y += player.movement_speed
         print("down")
    if keys[pygame.K_a]:
         player.x -= player.movement_speed
         print("left")
    if keys[pygame.K_d]:
         player.x += player.movement_speed
         print("right")

    screen.blit(player_img,(player.x, player.y))

    screen.blit(text,(0, 0))   

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
