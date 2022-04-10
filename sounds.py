import pygame


class Sounds(object):
    def __init__(self, game):
        self.game = game
        self.volume = 0.1

    def music(self):
        pygame.mixer.music.set_volume(self.volume)
        print(pygame.mixer.music.get_volume())
        if self.game.win == 1:
            pygame.mixer.music.load("Xs-s-qRtRn.mp3")
            pygame.mixer.music.play()
        elif self.game.win == 3:
            pygame.mixer.music.load("")
