import pygame


class Interface(object):

    def __init__(self, game):
        self.game = game

    def draw(self):
        pygame.draw.rect(self.game.screen, (50, 50, 50), pygame.Rect(0, 0, 800, 640))

