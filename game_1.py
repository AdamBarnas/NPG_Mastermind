import sys
import pygame
import pickle
from player import Player
from interface import Interface
from sounds import Sounds

print(pygame.__version__)

class Game(object):
    def __init__(self):
        #Conf
        self.res = (800, 640)
        self.tickrate = 1/120.0
        # 1/max_fps

        pygame.init()
        self.screen = pygame.display.set_mode(self.res)

        self.clock = pygame.time.Clock()
        self.cl_dt = 0.0

        self.kwadrat = pygame.Rect(30, 30, 42, 42)
        self.R = self.G = self.B = 255
        self.n = 0
        self.win = 0
        self.level = 0
        self.max = 12
        self.dif = [350, 300]

        self.player = Player(self)
        self.interface = Interface(self)
        self.sounds = Sounds(self)

        # Colours
        self.yellow = (255, 112, 67)
        self.red = (59, 206, 172)
        self.green = (14, 173, 105)
        self.blue = (248, 214, 176)
        self.orange = (238, 66, 102)
        self.purple = (84, 13, 110)
        self.white = (255, 255, 255)
        self.gray = (128, 128, 128)

        self.sounds.music()

        while True:
            # eventy
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.save()
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                    self.player.ruch("d")
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                    self.player.ruch("a")
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                    self.player.ruch("w")
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                    self.player.ruch("s")
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.player.ruch("space")
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    self.player.ruch("d")
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    self.player.ruch("a")
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    self.player.ruch("s")
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    self.player.ruch("w")
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                    self.player.ruch("back")
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    self.player.ruch("enter")
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.save()
                    sys.exit(0)
                '''elif event.type == pygame.KEYDOWN and event.key == pygame.K_x:
                    self.save()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_z:
                    self.read()'''
            # tick
            self.cl_dt += self.clock.tick()/1000
            while self.cl_dt > self.tickrate:
                self.tick()
                self.cl_dt -= self.tickrate

            # draw and sound
            self.screen.fill((0, 0, 0))
            self.draw()
            self.play()
            pygame.display.flip()

            # difficulty
            if self.level != 0 and self.win == 1:
                self.max = 8
            elif self.level != 0 and self.win == 3:
                self.max = 10
            elif self.level != 0 and self.win == 4:
                self.max = 12
    def tick(self):
        self.player.tick()
        if not pygame.mixer.music.get_busy():
            self.sounds.music()

    def draw(self):
        self.interface.draw()

        if self.level == 0:
            self.interface.difficulty()
        else:
            self.player.draw()

    def play(self):
        if self.win == 2:
            self.sounds.music()
            self.win = 0
        if self.win == 5:
            self.sounds.music()
            self.win = 6

    def forceplay(self):
        self.sounds.music()

    def save(self):
        pickle.dump(self.player.lista, open("savefiles/lista.data", "wb"))
        pickle.dump(self.player.odp, open("savefiles/odp.data", "wb"))
        pickle.dump(self.player.row, open("savefiles/row.data", "wb"))
        pickle.dump(self.player.col, open("savefiles/col.data", "wb"))
        pickle.dump(self.player.kombinacja, open("savefiles/kombinacja.data", "wb"))
        pickle.dump(self.win, open("savefiles/win.data", "wb"))

    def read(self):
        self.player.lista = pickle.load(open("savefiles/lista.data", "rb"))
        self.player.odp = pickle.load(open("savefiles/odp.data", "rb"))
        self.player.row = pickle.load(open("savefiles/row.data", "rb"))
        self.player.col = pickle.load(open("savefiles/col.data", "rb"))
        self.player.kombinacja = pickle.load(open("savefiles/kombinacja.data", "rb"))
        self.win = pickle.load(open("savefiles/win.data", "rb"))

    def clear(self):
        self.player.lista = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
                      [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.player.odp = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        self.player.kombinacja = [0, 0, 0, 0]
        self.player.row = self.player.col = self.win = 0

    def stat(self):
        if self.level == 2:
            f1 = open("savefiles/stat_row.txt", "at")
            f1.write(self.player.row)
            f1.close()
            f2 = open("savefiles/stat_win.txt", "at")
            f2.write(self.win)
            f2.close()

        else:
            f3 = open("savefiles/stat_difficulty.txt", "at")
            f3.write(self.win)
            f3.close()

    def showstat(self):
        pass


if __name__ == "__main__":
    Game()