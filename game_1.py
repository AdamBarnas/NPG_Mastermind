import sys
import pygame
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
        self.win = 3

        self.player = Player(self)
        self.interface = Interface(self)
        self.sounds = Sounds(self)

        # Colours
        self.yellow = (255, 255, 0)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.orange = (255, 128, 0)
        self.purple = (200, 0, 255)
        self.white = (255, 255, 255)
        self.gray = (128, 128, 128)

        self.sounds.music()

        while True:
            # eventy
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                    self.player.ruch("d")
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                    self.player.ruch("a")
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                    self.player.ruch("w")
                    self.sounds.music()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                    self.player.ruch("s")
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.player.ruch("space")
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    self.player.ruch("d")
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    self.player.ruch("a")
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                    self.player.ruch("b")
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    self.player.ruch("e")

            # tick
            self.cl_dt += self.clock.tick()/1000
            while self.cl_dt > self.tickrate:
                self.tick()
                self.cl_dt -= self.tickrate

            # draw
            self.screen.fill((0, 0, 0))
            self.draw()
            pygame.display.flip()

            if self.win == 2:
                self.sounds.music()
                self.win = 0

    def tick(self):
        self.player.tick()
        if not pygame.mixer.music.get_busy():
            self.sounds.music()

    def draw(self):
        self.interface.draw()
        self.player.draw()

if __name__ == "__main__":
    Game()