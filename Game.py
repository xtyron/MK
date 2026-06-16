import pygame
import json
from player import Player


player_img = pygame.image.load("res/player_forward_movement_1.PNG")

pygame.init()


player = Player("Masha", 100, 12)

clock = pygame.time.Clock()


with open("Cozy Garten\Startingmap.json", "r", encoding="utf-8") as f:
     starting_map = json.load(f)
     print(f"Map file opened, map looks like: {starting_map}\n maps length {len(starting_map)}")

rechtange_size = 32

def drawmap(surface, map_data : list):
     for i in range(len(map_data)):
          for j in range(len(map_data[i])):
               if map_data[i][j] == 1:
                    color = (255,255,255)
               elif map_data[i][j] == 6:
                    color = (20,20,20)
               else:
                    color = (0,0,0)
               
               pygame.draw.rect(surface, color, (j * rechtange_size, i * rechtange_size, rechtange_size, rechtange_size))


rechtange_amount = len(starting_map)


screen_height = rechtange_size * rechtange_amount
screen_width = rechtange_size * rechtange_amount

scale = 32

screen = pygame.display.set_mode((screen_height, screen_width))
pygame.display.set_caption("Cozy Garden")

running = True



font = pygame.font.SysFont(None, 20)



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    coordinates_in_str = "x: " + str(player.x) + " y: " + str(player.y)
    coordinates_in_str = font.render(coordinates_in_str, True, "red")

    drawmap(screen, starting_map)

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
    if keys[pygame.K_f]:
         with open("Cozy Garten/startingmap.json", "w") as f:
               starting_map[0][2] = 9
               json.dump(starting_map, f)
    if keys[pygame.K_x]:
         with open("Cozy Garten/startingmap.json", "w") as f:
               starting_map[0][2] = 1
               json.dump(starting_map, f)

    screen.blit(player_img,(player.x, player.y))

    screen.blit(coordinates_in_str, (0, 0))   

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
