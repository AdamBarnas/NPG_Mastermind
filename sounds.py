import pygame


class Sounds(object):
    def __init__(self, game):
        self.game = game
        self.volume = 0.1
        self.i = 0


    def music(self):

        if self.game.level == 0 or self.game.level == 3:
            pygame.mixer.music.set_volume(0.1)
            pygame.mixer.music.load("music/easy_4.mp3")
            pygame.mixer.music.play()

        else:
            pygame.mixer.music.stop()
            if self.game.win == 2:
                pygame.mixer.music.set_volume(0.1)
                # muzyka zwycięstwa
                pygame.mixer.music.load("music/win.mp3")
                pygame.mixer.music.play()

            if self.game.win == 5:
                pygame.mixer.music.set_volume(0.1)
                # muzyka przegranej
                pygame.mixer.music.load("music/defeat.mp3")
                pygame.mixer.music.play()

            elif self.game.win == 1:

                pygame.mixer.music.set_volume(0.15)
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
                pygame.mixer.music.set_volume(0.45)
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
