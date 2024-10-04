import pygame

class Ship:

    def __init__(self, ai_game):

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #load the ship image and get its rect
        # self.image = pygame.image.load('/img/spaceship.bmp')
        # self.image = pygame.image.load('alien_py\img\spaceship.bmp')
        self.image = pygame.image.load('alien_py\img\spaceship.png')
        self.image = pygame.transform.scale(self.image, (100, 100))


        self.rect = self.image.get_rect()

        #start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)

