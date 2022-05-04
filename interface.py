import pygame


class Interface(object):

    def __init__(self, game):
        self.game = game
        # Colours

        self.yellow = (255, 112, 23)
        self.red = (59, 206, 172)
        self.green = (14, 173, 105)
        self.blue = (248, 214, 176)
        self.orange = (238, 66, 102)
        self.purple = (84, 13, 110)
        self.white = (255, 255, 255)
        self.gray = (128, 128, 128)

    def draw(self):
        # print(self.game.win)
        if self.game.level == 0:
            pygame.draw.rect(self.game.screen, self.gray, (800, 640, 0, 0))
        else:
            font1 = 'fonts/Pixeltype.ttf'
            font_big = pygame.font.Font(font1, 50)
            font_mid = pygame.font.Font(font1, 40)
            font_small = pygame.font.Font(font1, 30)

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
                self.game.screen.blit(cow, (655, 250))

            if self.game.win == 0:
                wincow = pygame.image.load("img/easy_win_cow2.png")
                self.game.screen.blit(wincow, (280, 184))

            if self.game.win == 5:
                loosecow = pygame.image.load("img/easy_loose_cow2.png")
                self.game.screen.blit(loosecow, (280, 184))
