import pygame


class Interface(object):

    def __init__(self, game):
        self.game = game


    def difficulty(self):
        color = (self.game.R, self.game.G, self.game.B)
        pygame.draw.rect(self.game.screen, color, pygame.Rect(self.game.dif[0], self.game.dif[1], 100, 20))

    def draw(self):

        font1 = 'fonts/Pixeltype.ttf'
        font_big = pygame.font.Font(font1, 50)
        font_mid = pygame.font.Font(font1, 40)
        font_small = pygame.font.Font(font1, 30)

        if self.game.level == 0:
            # pygame.draw.rect(self.game.screen, self.gray, (800, 640, 0, 0))
            menu = pygame.image.load("img/menu.png")
            self.game.screen.blit(menu, (0, 0))

        elif self.game.level == 3:
            statistics = pygame.image.load("img/stats_bkg.png")
            self.game.screen.blit(statistics, (0, 0))
            tytul = font_big.render("STATISTICS", False, self.game.white)
            self.game.screen.blit(tytul, (300, 20))
            f1 = open("savefiles/stat_row.txt")
            f2 = open("savefiles/stat_win.txt")
            f3 = open("savefiles/stat_difficulty.txt")
            for i in range(15):
                numer = font_mid.render("Number of rounds:", False, self.game.white)
                numer_rzedu = font_mid.render(f1.readline(1), False, self.game.white)
                winlose = font_mid.render(f2.readline(4), False, self.game.white)
                difficulty = font_mid.render(f3.readline(6), False, self.game.white)
                self.game.screen.blit(numer, (50, 60 + i*35))
                self.game.screen.blit(numer_rzedu, (300, 60 + i*35))
                self.game.screen.blit(winlose, (350, 60 + i*35))
                self.game.screen.blit(difficulty, (450, 60 + i*35))

        else:

            if self.game.win == 3:
                background = pygame.image.load("img/easy_background.png")
                game_block = pygame.image.load("img/easy_game_rows.png")
                rules = pygame.image.load("img/easy_rules.png")
                result_block = pygame.image.load("img/easy_result.png")
                cow = pygame.image.load("img/easy_win_cow.png")

            if self.game.win == 1:
                background = pygame.image.load("img/hard_background.png")
                game_block = pygame.image.load("img/hard_game_rows.png")
                rules = pygame.image.load("img/hard_rules.png")
                result_block = pygame.image.load("img/hard_result.png")
                cow = pygame.image.load("img/easy_win_cow.png")

            if self.game.win == 4:
                background = pygame.image.load("img/veasy_background.png")
                game_block = pygame.image.load("img/veasy_game_rows.png")
                rules = pygame.image.load("img/veasy_rules.png")
                result_block = pygame.image.load("img/veasy_result.png")
                cow = pygame.image.load("img/easy_win_cow.png")

            if self.game.win == 1 or self.game.win == 3 or self.game.win == 4:
                self.game.screen.blit(background, (0, 0))
                self.game.screen.blit(game_block, (400 - 27, 15))
                self.game.screen.blit(rules, (29, 400))
                self.game.screen.blit(result_block, (600 - 8, 15))

            if self.game.win == 0:
                backgroundWin = pygame.image.load("img/win_bkg.png")
                self.game.screen.blit(backgroundWin, (0, 0))
                wincow = pygame.image.load("img/easy_win_cow2.png")
                self.game.screen.blit(wincow, (280, 150))


            if self.game.win == 6:
                backgroundLoose = pygame.image.load("img/loose_bkg.png")
                self.game.screen.blit(backgroundLoose, (0,0))
                loosecow = pygame.image.load("img/hard_loose_cow.png")
                self.game.screen.blit(loosecow, (280, 100))
