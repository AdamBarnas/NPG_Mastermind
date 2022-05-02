import pygame


class Menu(object):

    def __init__(self, game):
        self.game = game


    def difficulty(self):
        color = (self.game.R, self.game.G, self.game.B)
        pygame.draw.rect(self.game.screen, color, pygame.Rect(self.game.dif[0], self.game.dif[1] , 100, 20))