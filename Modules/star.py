"""import pygame"""
import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """Models star object"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #load the star image and set its rect attribute
        self.image = pygame.image.load('images/star.png')
        self.image = pygame.transform.scale(self.image, (10, 10))
        self.rect = self.image.get_rect()

        #set star rect at top left position
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #save exact position of star
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        """Draw the star at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Move the star down """
        self.y += self.settings.star_speed
        self.rect.y = self.y
