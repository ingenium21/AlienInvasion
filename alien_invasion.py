"""import system and pygame and settings"""
import sys
import pygame
from Modules.settings import Settings
from Modules.ship import Ship
from Modules.bullets import Bullet

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
        #import the bullet sprites
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            #Watch for keyboard and mouse events
            self._check_events()
            self.ship.update()
            self._update_bullets()
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
        """Update images on the screen and flip to a new screen"""
        #Redarw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        #draw the ship
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        #Make the most recently drawn screen visible
        pygame.display.flip()
    
    def _check_keydown_events(self, event):
        """Respond to keypress down events"""
        if event.key == pygame.K_RIGHT:
        #Move the ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
        #Move the ship to the left
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_f:
            #changes it to fullscreen, it sort of works but not really, will need to rework this in the future
            #currently changes it to fullscreen but the game's resolution is still set to the original window
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
            
    
    def _check_keyup_events(self,event):
        """Respond to keypress releases"""
        #stop moving the ship
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets"""
        #update bullet positions
        self.bullets.update()
        #Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

if __name__ == '__main__':
    #Make a game instance,and then run the game
    AI = AlienInvasion()
    AI.run_game()
