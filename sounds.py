import pygame


class Sounds(object):
    def __init__(self, game):
        self.game = game
        self.volume = 0.1

    def music(self):
        # print(pygame.mixer.music.get_volume())
        if self.game.win == 2:

            # muzyka zwycięstwa
<<<<<<< Updated upstream
            pygame.mixer.music.load("music/Xs-s-qRtRn.mp3")
=======
            pygame.mixer.music.set_volume(self.volume)
            pygame.mixer.music.load("music/win.mp3")
            pygame.mixer.music.play()
>>>>>>> Stashed changes

        elif self.game.win == 1:

            pygame.mixer.music.set_volume(0.15)
<<<<<<< Updated upstream
            # muzyka tło
            pygame.mixer.music.load("music/Regular_Show.mp3")
            pygame.mixer.music.queue("music/Regular_Show.mp3", loops=10)
        pygame.mixer.music.play()
=======
            # muzyka hard

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

        elif self.game.win == 3:
            pygame.mixer.music.set_volume(0.15)
            # muzyka medium

            if self.i == 0:
                pygame.mixer.music.load("music/medium_1.mp3")
                self.i = 1
            elif self.i == 1:
                pygame.mixer.music.load("music/medium_2.mp3")
                self.i = 2
            elif self.i == 2:
                pygame.mixer.music.load("music/medium_3.mp3")
                self.i = 0
            pygame.mixer.music.play()

        elif self.game.win == 4:
            pygame.mixer.music.set_volume(0.35)
            # muzyka easy

            if self.i == 0:
                pygame.mixer.music.load("music/easy_1.mp3")
                self.i = 1
            elif self.i == 1:
                pygame.mixer.music.load("music/easy_2.mp3")
                self.i = 2
            elif self.i == 2:
                pygame.mixer.music.load("music/easy_3.mp3")
                self.i = 0
            pygame.mixer.music.play()
>>>>>>> Stashed changes
