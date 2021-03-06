import pygame.font

class Button:
    def __init__(self, ai_game, msg, pos="midbottom"):
        """Initialize button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        #set the dimensions and propoerties of the button.
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        #Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        
        #give button the pos attribute
        if pos == "center":
            self.rect.center = self.screen_rect.center
        elif pos == "topleft":
            self.rect.topleft = self.screen_rect.topleft
        elif pos == "midtop":
            self.rect.midtop = self.screen_rect.midtop
        elif pos == "topright":
            self.rect.topright = self.screen_rect.topright
        elif pos == "midleft":
            self.rect.midleft = self.screen_rect.midleft
        elif pos == "midright":
            self.rect.midright = self.screen_rect.midright
        elif pos == "midbottom":
            self.rect.midbottom = self.screen_rect.midbottom
            self.rect.move_ip(0, -150)

        #The button message needs to be prepped only once.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, None)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    
    def draw_button(self):
        #draw a blank button and then draw message
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)