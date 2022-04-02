import sys

import pygame

print(pygame.__version__)

screen = pygame.display.set_mode((800,640))

while True:
    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
    # draw
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(10,20,200,100))
    pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(210, 20, 200, 100))
    pygame.display.flip()