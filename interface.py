import pygame


class Interface(object):

    def __init__(self, game):
        self.game = game
        # Colours

        self.yellow = (255, 255, 0)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.orange = (255, 128, 0)
        self.purple = (200, 0, 255)
        self.white = (255, 255, 255)
        self.gray = (128, 128, 128)

    def draw(self):
        background_easy = pygame.image.load("img/easy_background.png")
        self.game.screen.blit(background_easy, (0,0))

        game_block = pygame.image.load("img/easy_game_rows.png")
        self.game.screen.blit(game_block, (400-35,15))

        rules_easy = pygame.image.load("img/easy_rules.png")
        rules_easy = pygame.transform.rotate(rules_easy, 90)
        self.game.screen.blit(rules_easy, (29, 400))
