import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 640))

print(pygame.__version__)

kwadrat = pygame.Rect(10, 20, 100, 100)
R = G = B = 255
n = 0
clock = pygame.time.Clock()
dt = 0.0
rain = 0.0

tick = 1/40.0
# 1/max_fps

while True:
    # eventy
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_x:
            kwadrat.y += 10
    # input
    inkey = pygame.key.get_pressed()

    # tickrate
    dt += clock.tick()/1000.0
    while dt > tick:
        dt -= tick
        # move

        speed = 5

        if inkey[pygame.K_a]:
            kwadrat.x -= speed
        if inkey[pygame.K_s]:
            kwadrat.y += speed
        if inkey[pygame.K_d]:
            kwadrat.x += speed
        if inkey[pygame.K_w]:
            kwadrat.y -= speed

        # borders
        if kwadrat.x <= -50:
            kwadrat.x = 750
        if kwadrat.y <= 0:
            kwadrat.y = 640
        if kwadrat.x >= 801:
            kwadrat.x = 0
        if kwadrat.y >= 641:
            kwadrat.y = 0


        # rainbow
        if n < 250:
            R -= 4
            G -= 4
            B -= 4
        elif n < 500:
            R += 4
            G += 4
            B += 4
        else:
            n = 0
        n += 4

    # draw
    kolor = (R, G, B)
    pygame.draw.rect(screen, kolor, kwadrat)
    pygame.display.flip()
    screen.fill((0, 0, 0))
