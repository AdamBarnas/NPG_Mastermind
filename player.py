import random
import pygame
from pygame.math import Vector2

class Player(object):

    def __init__(self, game):
        self.game = game

        self.pos = Vector2(29, 29)
        self.game.kwadrat.x = self.pos[0]
        self.game.kwadrat.y = self.pos[1]
        self.n = self.col = self.row = self.drift = 0
        self.addon = 0
        self.lista = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.odp = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        self.kombinacja = [0, 0, 0, 0]
        self.good = 0
        self.ok = 0

        self.szyfr()
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

        # nowy wiersz
        if self.lista[self.row][3] != 0:
            self.spr()
            self.row += 1
            self.col = 0

    # ustawianie kombinacji
    def szyfr(self):
        self.kombinacja = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
        for t in range(2):
            for i in range(4):
                for j in range(4):
                    if self.kombinacja[i] == self.kombinacja[j] and i != j:
                        if self.kombinacja[j] == 6:
                            self.kombinacja[j] = 1
                        else:
                            self.kombinacja[j] += 1
        print(self.kombinacja)

    def ruch(self, direction):
        '''if direction == "w":
           self.game.kwadrat.y -= 50
        elif direction == "s":
            self.game.kwadrat.y += 50'''
        if direction == "d" and self.game.kwadrat.x < 279:
            self.game.kwadrat.x += 50
        elif direction == "a" and self.game.kwadrat.x > 30:
            self.game.kwadrat.x -= 50
        elif direction == "space":

            # wybór koloru
            if self.game.kwadrat.x == 29:
                self.lista[self.row][self.col] = 1
            elif self.game.kwadrat.x == 79:
                self.lista[self.row][self.col] = 2
            elif self.game.kwadrat.x == 129:
                self.lista[self.row][self.col] = 3
            elif self.game.kwadrat.x == 179:
                self.lista[self.row][self.col] = 4
            elif self.game.kwadrat.x == 229:
                self.lista[self.row][self.col] = 5
            elif self.game.kwadrat.x == 279:
                self.lista[self.row][self.col] = 6
            self.col += 1
            self.drift = 50
            print(self.lista)


        # współrzędne myszy
        # print(pygame.mouse.get_pos())

    def spr(self):
        self.ok = self.good = 0
        for i in range(4):
            if self.kombinacja[i] == self.lista[self.row][i]:
                self.good += 1
            for j in range(4):
                if self.kombinacja[i] == self.lista[self.row][j] and j != i:
                    self.ok += 1
        '''print(self.good)
        print(self.ok)'''
        self.odp[self.row] = [self.good, self.ok]
        print(self.odp)

    def draw(self):
        color = (self.game.R, self.game.G, self.game.B)
        pygame.draw.rect(self.game.screen, color, self.game.kwadrat)

        # interface
        pygame.draw.circle(self.game.screen, self.game.yellow, (50, 50), 20)
        pygame.draw.circle(self.game.screen, self.game.red, (100, 50), 20)
        pygame.draw.circle(self.game.screen, self.game.orange, (150, 50), 20)
        pygame.draw.circle(self.game.screen, self.game.blue, (200, 50), 20)
        pygame.draw.circle(self.game.screen, self.game.green, (250, 50), 20)
        pygame.draw.circle(self.game.screen, self.game.purple, (300, 50), 20)

        # new ones
        for j in range(0, self.row + 1):
            d = 0
            for i in range(0, 4):
                if self.lista[j][i] == 1:
                    pygame.draw.circle(self.game.screen, self.game.yellow, (400 + i*self.drift, 50 + j*self.drift), 20)
                elif self.lista[j][i] == 2:
                    pygame.draw.circle(self.game.screen, self.game.red, (400 + i*self.drift, 50 + j*self.drift), 20)
                elif self.lista[j][i] == 3:
                    pygame.draw.circle(self.game.screen, self.game.orange, (400 + i*self.drift, 50 + j*self.drift), 20)
                elif self.lista[j][i] == 4:
                    pygame.draw.circle(self.game.screen, self.game.blue, (400 + i*self.drift, 50 + j*self.drift), 20)
                elif self.lista[j][i] == 5:
                    pygame.draw.circle(self.game.screen, self.game.green, (400 + i*self.drift, 50 + j*self.drift), 20)
                elif self.lista[j][i] == 6:
                    pygame.draw.circle(self.game.screen, self.game.purple, (400 + i*self.drift, 50 + j*self.drift), 20)

            # wyniki

            if self.odp[j][0] >= 1:
                pygame.draw.circle(self.game.screen, self.game.white, (600, 40 + self.drift * j), 8)
                if self.odp[j][0] >= 2:
                    pygame.draw.circle(self.game.screen, self.game.white, (600, 60 + self.drift * j), 8)
                    if self.odp[j][0] >= 3:
                        pygame.draw.circle(self.game.screen, self.game.white, (620, 40 + self.drift * j), 8)
                        if self.odp[j][0] == 4:
                            pygame.draw.circle(self.game.screen, self.game.white, (620, 60 + self.drift * j), 8)

                            # wygrana
                            if self.game.win == 1:
                                self.game.win = 2

                            win_image = pygame.image.load("img/easy_win_cow.png")
                            self.game.screen.blit(win_image,(400,320))

                        elif self.odp[j][1] == 1:
                            pygame.draw.circle(self.game.screen, self.game.gray, (620, 60 + self.drift * j), 8)
                    elif self.odp[j][1] >= 1:
                        pygame.draw.circle(self.game.screen, self.game.gray, (620, 40 + self.drift * j), 8)
                        if self.odp[j][1] == 2:
                            pygame.draw.circle(self.game.screen, self.game.gray, (620, 60 + self.drift * j), 8)
                elif self.odp[j][1] >= 1:
                    pygame.draw.circle(self.game.screen, self.game.gray, (600, 60 + self.drift * j), 8)
                    if self.odp[j][1] >= 2:
                        pygame.draw.circle(self.game.screen, self.game.gray, (620, 40 + self.drift * j), 8)
                        if self.odp[j][1] == 3:
                            pygame.draw.circle(self.game.screen, self.game.gray, (620, 60 + self.drift * j), 8)
            elif self.odp[j][1] >= 1:
                pygame.draw.circle(self.game.screen, self.game.gray, (600, 40 + self.drift * j), 8)
                if self.odp[j][1] >= 2:
                    pygame.draw.circle(self.game.screen, self.game.gray, (600, 60 + self.drift * j), 8)
                    if self.odp[j][1] >= 3:
                        pygame.draw.circle(self.game.screen, self.game.gray, (620, 40 + self.drift * j), 8)
                        if self.odp[j][1] == 4:
                            pygame.draw.circle(self.game.screen, self.game.gray, (620, 60 + self.drift * j), 8)
