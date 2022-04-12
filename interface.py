import pygame


class Interface(object):

    def __init__(self, game):
        self.game = game
        # Colours

        self.yellow = (255, 147, 23)
        self.red = (59, 206,172)
        self.green = (14, 173, 105)
        self.blue = (248, 214, 176)
        self.orange = (238, 66, 102)
        self.purple = (84, 13, 110)
        self.white = (255, 255, 255)
        self.gray = (128, 128, 128)

    def draw(self):
        background_easy = pygame.image.load("img/easy_background.png")
        self.game.screen.blit(background_easy, (0,0))

        game_block = pygame.image.load("img/easy_game_rows.png")
        self.game.screen.blit(game_block, (400-35,8))

        rules_easy = pygame.image.load("img/easy_rules.png")
        rules_easy = pygame.transform.rotate(rules_easy, 90)
        self.game.screen.blit(rules_easy, (29, 400))

        result_block = pygame.image.load("img/easy_result.png")
        self.game.screen.blit(result_block, (600-8,15))