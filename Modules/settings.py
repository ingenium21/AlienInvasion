class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings"""
        #Screen Settings
        self.screen_width = 1024
        self.screen_height = 768
        self.bg_color = (32, 32, 32)

        #ship settings
        self.ship_speed = 1.5
        self.ship_limit = 2
        
        #Bullet Settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 255, 255)
        self.bullets_allowed = 4

        #alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #fleet direction of 1 represents right, -1 represents left
        self.fleet_direction = 1

        #how quickly the game speeds up
        self.speedup_scale = 1.1

        #set difficulty
        self.difficulty_settings = False

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game for Normal difficulty"""
        self.bullet_speed = 2.5
        self.ship_speed = 1.5
        self.alien_speed = 1.0
        self.alien_points = 50
        #fleet direction of 1 represents right, -1 represents left
        self.fleet_direction = 1

    def increase_speed(self):
        """increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
    
    def initialize_easy_settings(self):
        """Initialize settings that change throughout the game for Easy difficulty."""
        self.bullet_speed = 3.0
        self.ship_speed = 1.5
        self.alien_speed = 1.0
        self.alien_points = 100

        #fleet direction of 1 represents right, -1 represents left
        self.fleet_direction = 1
    
    def initialize_hard_settings(self):
        """Initialize settings that change throughout the game for Hard difficulty."""
        self.bullet_speed = 1.0
        self.ship_speed = 2.0
        self.alien_speed = 3.0
        self.alien_points = 150

        #fleet direction of 1 represents right, -1 represents left
        self.fleet_direction = 1
    