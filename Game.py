import pygame


pygame.init()

x = 0
y = 0

rechtange_size = 32
rechtange_amount = 32

screen_height = rechtange_size * rechtange_amount
screen_width = rechtange_size * rechtange_amount

scale = 32

screen = pygame.display.set_mode((screen_height, screen_width))
pygame.display.set_caption("Cozy Garden")

running = True


screen.fill((0,0,0))

for i in range(3):
    x = 0
    if i != 0:
        y += rechtange_size
    for j in range(scale):
            pygame.draw.rect(screen,(0,250,0),(x, y, rechtange_size, rechtange_size))
            pygame.draw.rect(screen,(0,0,0), (x+1, y+1, rechtange_size - 2, rechtange_size - 2))
            x += rechtange_size

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        

    pygame.display.flip()

pygame.quit()
