import pygame


class Sounds(object):
    def __init__(self, game):
        self.game = game
        self.volume = 0.1
        self.i = 0

    def music(self):
        pygame.mixer.music.set_volume(self.volume)
        # print(pygame.mixer.music.get_volume())
        if self.game.win == 2:

            # muzyka zwycięstwa
            pygame.mixer.music.load("music/win.mp3")
            pygame.mixer.music.play()

        elif self.game.win == 1:

            pygame.mixer.music.set_volume(0.15)
            # muzyka tło

            if self.i == 0:
                pygame.mixer.music.load("music/hard_1.mp3")
                self.i = 1
            elif self.i == 1:
                pygame.mixer.music.load("music/hard_2.mp3")
                self.i = 2
            elif self.i == 2:
                pygame.mixer.music.load("music/hard_3.mp3")
                self.i = 0
            pygame.mixer.music.play()
