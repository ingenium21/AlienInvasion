"""import system and pygame and settings"""
import sys
import pygame
from Modules.settings import Settings
from Modules.ship import Ship

class AlienInvasion:
    """Overrall class to manage game assets and behavior"""

    def __init__(self):
        """initialize the game, and create game resources"""
        pygame.init()
        self.settings = Settings()

        #sets the window size and caption
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Spuds Invasion")

        #import the ship and make an instance of it
        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            #Watch for keyboard and mouse events
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _update_screen(self):
        """Update images on teh screen and flip to a new screen"""
        #Redarw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        #draw the ship
        self.ship.blitme()
        #Make the most recently drawn screen visible
        pygame.display.flip()
    
    def _check_keydown_events(self, event):
        """Respond to keypress down events"""
        if event.key == pygame.K_RIGHT:
        #Move the ship to the right
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
        #Move the ship to the left
            self.ship.moving_left = True
    
    def _check_keyup_events(self,event):
        """Respond to keypress releases"""
        #stop moving the ship
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False


if __name__ == '__main__':
    #Make a game instance,and then run the game
    AI = AlienInvasion()
    AI.run_game()
