"""Import pygame"""
import pygame
class Ship:
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #movement flags
        self.moving_right = False
        self.moving_left = False

        # Load the ship(feelsCoolMan) image and gets its rect.
        self.image = pygame.image.load('images/feelsCoolMan.bmp')
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = self.image.get_rect()

        #Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #Store a decimal value of the ship's horizontal position
        self.x = float(self.rect.x)


    def update(self):
        """Update the ship's position based on the movement flags"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        #Update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
        