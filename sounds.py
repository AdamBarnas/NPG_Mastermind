import pygame


class Sounds(object):
    def __init__(self, game):
        self.game = game
        self.volume = 0.1

    def music(self):
        pygame.mixer.music.set_volume(self.volume)
        # print(pygame.mixer.music.get_volume())
        if self.game.win == 2:

            # muzyka zwycięstwa
            pygame.mixer.music.load("music/Xs-s-qRtRn.mp3")

        elif self.game.win == 1:

            pygame.mixer.music.set_volume(0.5)
            #muzyka tło
            pygame.mixer.music.load("music/Regular_Show.mp3")
        pygame.mixer.music.play()
