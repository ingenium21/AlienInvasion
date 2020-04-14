"""import system and pygame and settings"""
import sys
from time import sleep
import pygame
import random

from Modules.settings import Settings
from Modules.ship import Ship
from Modules.bullets import Bullet
from Modules.alien import Alien
from Modules.game_stats import GameStats
from Modules.star import Star
from Modules.button import Button

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

        #Create an instance to store game statistics
        self.stats = GameStats(self)

        #import the stars
        self.stars = pygame.sprite.Group()
        self._create_stars()
        #import the ship and make an instance of it
        self.ship = Ship(self)
        #import the bullet sprites
        self.bullets = pygame.sprite.Group()
        #import the alien sprites
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        #import the stars
        self._create_stars()
        #create the play button
        self.play_button = Button(self, "Play")
        #difficulty buttons
        self.easy_button = Button(self, "Easy", "topleft")
        self.normal_button = Button(self, "Normal", "midtop")
        self.hard_button = Button(self, "Hard", "topright")


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            #Watch for keyboard and mouse events
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                self._check_easy_button(mouse_pos)
                self._check_normal_button(mouse_pos)
                self._check_hard_button(mouse_pos)

    def _update_screen(self):
        """Update images on the screen and flip to a new screen"""
        #Redarw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        #draw the stars
        self.stars.draw(self.screen)
        #draw the ship
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        #draw the aliens
        self.aliens.draw(self.screen)

        #draw the play button
        if not self.stats.game_active and not self.settings.difficulty_settings:
            self.play_button.draw_button()

        elif self.settings.difficulty_settings and not self.stats.game_active:
            self.easy_button.draw_button()
            self.normal_button.draw_button()
            self.hard_button.draw_button()
            
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
        elif event.key == pygame.K_p and not self.stats.game_active:
            self._start_game()
            
    
    def _check_keyup_events(self, event):
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
        
        self._check_bullet_alien_collisions()
    
    def _create_fleet(self):
        """Create the fleet of aliens."""
        #Make an alien
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        ship_height = self.ship.rect.height
        #get the number of aliens across
        available_space_x = self.settings.screen_width - (2* alien_width)
        number_aliens_x = available_space_x // int((2*alien_width))

        #get the number of aliens from top to bottom
        available_space_y = self.settings.screen_height - (3 * alien_height) - ship_height
        number_rows = available_space_y // (2*alien_height)

        #Create the full fleet of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)
    
    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in the row."""
        alien = Alien(self)
        alien_width = alien.rect.width
        alien.x = alien_width + 2*alien_width*alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_aliens(self):
        """
        Check if the fleet is at an edge,
        then update the positions of all aliens in the fleet
        """
        self._check_fleet_edges()
        self.aliens.update()

        #look for alien-ship collision
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        
        #look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()

    
    def _create_stars(self):
        """Create a fleet of stars and place them in their random locations"""
        #Make a star
        for _ in range(20):
            star = Star(self)
            star.rect.x = random.randint(1, self.settings.screen_width)
            star.rect.y = random.randint(1, self.settings.screen_width)
            self.stars.add(star)
    
    
    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    
    def _check_bullet_alien_collisions(self):
        #Check for any bullets that have hit aliens.
        #If so, get rid of the bullet and the alien
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            #Destroy existing bullets and create a new fleet.
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
    
    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            #decrease ships_left
            self.stats.ships_left -= 1
            #Get rid of any emaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()
            #create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()
            #Pause.
            sleep(0.5)
        
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
    
    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                #treat this the same as if the ship got hit.
                self._ship_hit()
                break
    
    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.settings.difficulty_settings = True
    
    def _check_easy_button(self, mouse_pos):
        button_clicked = self.easy_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            #Reset the game statistics with easy settings
            self.settings.initialize_easy_settings()
            self._start_game()
    
    def _check_normal_button(self, mouse_pos):
        button_clicked = self.normal_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            #Reset the game settings with normal settings
            self.settings.initialize_dynamic_settings()
            self._start_game()
    
    def _check_hard_button(self, mouse_pos):
        button_clicked = self.hard_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            #Reset the game settings with hard settings
            self.settings.initialize_hard_settings()
            self._start_game()

            

    def _start_game(self):
        #reset the game statistics
        self.stats.reset_stats()
        self.stats.game_active = True
        #Get rid of any remaining aliens and bullets.
        self.aliens.empty()
        self.bullets.empty()
        #Create a new fleet and center the ship
        self._create_fleet()
        self.ship.center_ship()
        #hide the mouse cursor
        pygame.mouse.set_visible(False)


if __name__ == '__main__':
    #Make a game instance,and then run the game
    AI = AlienInvasion()
    AI.run_game()
