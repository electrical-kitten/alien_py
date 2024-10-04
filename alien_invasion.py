import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    '''Overall classto manage game assets and behavior'''

    def __init__(self):
        '''initialize game and create game resouces'''
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height
            ), pygame.RESIZABLE)
        
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        
        # set background color
        # self.bg_color = (self.settings.bg_color)

    def run_game(self):
        '''Start main loop for the game'''
        while True:
            # Watch for keyborad and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # redraw the screen during each passthrough the loop
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # make the most recetly drawn screen visible
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    # make a game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()