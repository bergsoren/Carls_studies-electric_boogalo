class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start Alien Invasion in an inactive state
        self.game_active = False

        # High score should never be reset
        self.high_score = 0  # this is initialized once the object is instantiated and not reset

    def reset_stats(self):
        """Initialize statistics that can change in the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0