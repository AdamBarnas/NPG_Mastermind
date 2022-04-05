import pygame
from pygame.math import Vector2
class Player(object):

    def __init__(self, game):
        self.game = game

        self.pos = Vector2(29, 29)
        self.game.kwadrat.x = self.pos[0]
        self.game.kwadrat.y = self.pos[1]
        self.addon = self.n = self.drift = 0

    def tick(self):
        # input
        '''inkey = pygame.key.get_pressed()

        if inkey[pygame.K_a]:
            self.game.kwadrat.x -= 1
        if inkey[pygame.K_d]:
            self.game.kwadrat.x += 1
        if inkey[pygame.K_w]:
            self.game.kwadrat.y -= 1
        if inkey[pygame.K_s]:
            self.game.kwadrat.y += 1'''
        '''speed = 1

        if inkey[pygame.K_a]:
            self.game.kwadrat.x -= speed
        if inkey[pygame.K_s]:
            self.game.kwadrat.y += speed
        if inkey[pygame.K_d]:
            self.game.kwadrat.x += speed
        if inkey[pygame.K_w]:
            self.game.kwadrat.y -= speed'''

        '''# borders
        if self.game.kwadrat.x <= -50:
            self.game.kwadrat.x = 750
        if self.game.kwadrat.y <= -50:
            self.game.kwadrat.y = 590
        if self.game.kwadrat.x >= 751:
            self.game.kwadrat.x = -49
        if self.game.kwadrat.y >= 591:
            self.game.kwadrat.y = -49'''

        # rainbow

        if self.game.n < 250:
            self.game.R -= 4
            self.game.G -= 4
            self.game.B -= 4
        elif self.game.n < 500:
            self.game.R += 4
            self.game.G += 4
            self.game.B += 4
        else:
            self.game.n = 0
        self.game.n += 4

    def ruch(self, direction):
        if direction == "w":
            self.game.kwadrat.y -= 50
        elif direction == "s":
            self.game.kwadrat.y += 50
        elif direction == "d":
            self.game.kwadrat.x += 50
        elif direction == "a":
            self.game.kwadrat.x -= 50
        elif direction == "space":
            if self.game.kwadrat.x >= 29 and self.game.kwadrat.x <= 30:
                self.addon = 1
            elif self.game.kwadrat.x >= 79 and self.game.kwadrat.x <= 80:
                self.addon = 2
            elif self.game.kwadrat.x >= 129 and self.game.kwadrat.x <= 130:
                self.addon = 3
            elif self.game.kwadrat.x >= 179 and self.game.kwadrat.x <= 180:
                self.addon = 4
            elif self.game.kwadrat.x >= 229 and self.game.kwadrat.x <= 230:
                self.addon = 5
            elif self.game.kwadrat.x >= 279 and self.game.kwadrat.x <= 280:
                self.addon = 6
            self.n += 1
            self.drift = 50
        print(self.game.kwadrat.x)

    def draw(self):
        color = (self.game.R, self.game.G, self.game.B)
        pygame.draw.rect(self.game.screen, color, self.game.kwadrat)

        # Colours
        self.yellow = (255, 255, 0)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.orange = (255, 128, 0)
        self.purple = (200, 0, 255)

        # interface
        pygame.draw.circle(self.game.screen, self.yellow, (50, 50), 20)
        pygame.draw.circle(self.game.screen, self.red, (100, 50), 20)
        pygame.draw.circle(self.game.screen, self.orange, (150, 50), 20)
        pygame.draw.circle(self.game.screen, self.blue, (200, 50), 20)
        pygame.draw.circle(self.game.screen, self.green, (250, 50), 20)
        pygame.draw.circle(self.game.screen, self.purple, (300, 50), 20)

        # new ones
        for i in range(0, self.n):
            if self.addon == 1:
                pygame.draw.circle(self.game.screen, self.yellow, (300 + i*(self.drift), 300), 20)
            elif self.addon == 2:
                pygame.draw.circle(self.game.screen, self.red, (300 + i*(self.drift), 300), 20)
            elif self.addon == 3:
                pygame.draw.circle(self.game.screen, self.orange, (300 + i*(self.drift), 300), 20)
            elif self.addon == 4:
                pygame.draw.circle(self.game.screen, self.blue, (300 + i*(self.drift), 300), 20)
            elif self.addon == 5:
                pygame.draw.circle(self.game.screen, self.green, (300 + i*(self.drift), 300), 20)
            elif self.addon == 6:
                pygame.draw.circle(self.game.screen, self.purple, (300 + i*(self.drift), 300), 20)