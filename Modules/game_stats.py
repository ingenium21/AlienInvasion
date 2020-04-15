import json

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize the statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        #Start Alien Invasion in an active state.
        self.game_active = False

        #High Score should never be reset.
        self.high_score = 0

        #get the stored high score
        self.get_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        
        #player score
        self.score = 0
        self.level = 1
    
    def get_high_score(self):
        filename = 'json/high_score.json'
        with open(filename) as f:
            self.high_score = int(json.load(f))
    
    def save_high_score(self):
        filename = 'json/high_score.json'
        with open(filename, 'w') as f:
            json.dump(self.high_score, f)