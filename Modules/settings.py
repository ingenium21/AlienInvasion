class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings"""
        #Screen Settings
        self.screen_width = 1024
        self.screen_height = 768
        self.bg_color = (230, 230, 230)

        #ship settings
        self.ship_speed = 1.5
        self.ship_limit = 2
        
        #Bullet Settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 4

        #alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #fleet direction of 1 represents right, -1 represents left
        self.fleet_direction = 1

