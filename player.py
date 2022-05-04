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
        self.lista = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
                      [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.odp = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        self.kombinacja = [0, 0, 0, 0]
        self.good = 0
        self.ok = 0
        self.raz = 0
        self.xdis = 612
        self.zmienna = 0
        self.game.max = 12

        self.szyfr()

    def tick(self):

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
        if self.game.level == 0:
            if direction == "d" and self.game.dif[0] < 450:
                self.game.dif[0] += 100
            elif direction == "a" and self.game.dif[0] > 250:
                self.game.dif[0] -= 100

            elif direction == "enter":
                self.game.level = 1
                if self.game.dif[0] == 350:
                    self.game.win = 3
                elif self.game.dif[0] == 250:
                    self.game.win = 4
                elif self.game.dif[0] == 450:
                    self.game.win = 1
                self.game.forceplay()

        else:
            if direction == "d" and self.game.kwadrat.x < 279:
                self.game.kwadrat.x += 50
            elif direction == "a" and self.game.kwadrat.x > 30:
                self.game.kwadrat.x -= 50
            elif direction == "back":
                print("cofnij")
                if 0 < self.col <= 4:
                    self.col -= 1
                    self.lista[self.row][self.col] = 0

            elif direction == "enter":
                print("zapisz")

                # nowy wiersz
                if self.lista[self.row][3] != 0 and self.row < self.game.max:
                    self.spr()
                    self.row += 1
                    self.col = 0

            elif direction == "space" and self.row < self.game.max:
                if not self.lista[self.row][3] != 0:

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
        if self.row < self.game.max:
            self.zmienna = self.row + 1
        else:
            self.zmienna = self.row

        for j in range(0, self.row + 1):
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
                pygame.draw.circle(self.game.screen, self.game.white, (self.xdis, 40 + self.drift * j), 8)
                if self.odp[j][0] >= 2:
                    pygame.draw.circle(self.game.screen, self.game.white, (self.xdis, 60 + self.drift * j), 8)
                    if self.odp[j][0] >= 3:
                        pygame.draw.circle(self.game.screen, self.game.white, (self.xdis + 20, 40 + self.drift * j), 8)
                        if self.odp[j][0] == 4:
                            pygame.draw.circle(self.game.screen, self.game.white, (self.xdis + 20, 60 + self.drift * j), 8)

                            # wygrana
                            if self.game.win == 1 or self.game.win == 3 or self.game.win == 4:
                                self.game.win = 2
                                wincow = pygame.image.load("img/easy_win_cow2.png")
                                self.game.screen.blit(wincow, (280, 184))
                                print("wygrana")

                        elif self.odp[j][1] == 1:
                            pygame.draw.circle(self.game.screen, self.game.gray, (self.xdis + 20, 60 + self.drift * j), 8)
                    elif self.odp[j][1] >= 1:
                        pygame.draw.circle(self.game.screen, self.game.gray, (self.xdis + 20, 40 + self.drift * j), 8)
                        if self.odp[j][1] == 2:
                            pygame.draw.circle(self.game.screen, self.game.gray, (self.xdis + 20, 60 + self.drift * j), 8)
                elif self.odp[j][1] >= 1:
                    pygame.draw.circle(self.game.screen, self.game.gray, (self.xdis, 60 + self.drift * j), 8)
                    if self.odp[j][1] >= 2:
                        pygame.draw.circle(self.game.screen, self.game.gray, (self.xdis + 20, 40 + self.drift * j), 8)
                        if self.odp[j][1] == 3:
                            pygame.draw.circle(self.game.screen, self.game.gray, (self.xdis + 20, 60 + self.drift * j), 8)
            elif self.odp[j][1] >= 1:
                pygame.draw.circle(self.game.screen, self.game.gray, (self.xdis, 40 + self.drift * j), 8)
                if self.odp[j][1] >= 2:
                    pygame.draw.circle(self.game.screen, self.game.gray, (self.xdis, 60 + self.drift * j), 8)
                    if self.odp[j][1] >= 3:
                        pygame.draw.circle(self.game.screen, self.game.gray, (self.xdis + 20, 40 + self.drift * j), 8)
                        if self.odp[j][1] == 4:
                            pygame.draw.circle(self.game.screen, self.game.gray, (self.xdis + 20, 60 + self.drift * j), 8)
            # przegrana
            if self.row == self.game.max:
                print(self.game.win)
                if j == self.row - 1 and self.game.win == 1 or self.game.win == 3 or self.game.win == 4:
                    self.game.win = 5
