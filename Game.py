import pygame


pygame.init()

x = 0
y = 0

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Cozy Garden")

rechtange_size = 15

running = True


screen.fill((0,0,0))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for i in range(5):
        pygame.draw.rect(screen,(0,250,0),(x,y,rechtange_size,rechtange_size))
        x += 16
        y += 16

    pygame.display.flip()

pygame.quit()
