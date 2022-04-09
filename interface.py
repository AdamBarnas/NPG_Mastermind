import pygame
from player import Player


class Interface(object):

    def __init__(self, game):
        self.game = game

        # Colours
        self.yellow = (255, 255, 0)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.orange = (255, 128, 0)
        self.purple = (200, 0, 255)
        self.white = (255, 255, 255)
        self.gray = (128, 128, 128)

    def draw(self):
        pygame.draw.rect(self.game.screen, self.gray, pygame.Rect(0, 0, 400, 320))
