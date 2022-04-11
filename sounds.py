import pygame


class Sounds(object):
    def __init__(self, game):
        self.game = game
        self.volume = 0.1

    def music(self):
        pygame.mixer.music.set_volume(self.volume)
        # print(pygame.mixer.music.get_volume())
        if self.game.win == 1:

            # muzyka zwycięstwa
            pygame.mixer.music.load("music/Xs-s-qRtRn.mp3")
            pygame.mixer.music.play()
        elif self.game.win == 3:

            #muzyka tło
            pygame.mixer.music.load("")
