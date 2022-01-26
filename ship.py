import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """A class to manage the ship"""

    def __init__(self, ai_game, imagepath):

        """Initialize the ship with its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image
        self.image = pygame.image.load(imagepath)
        self.rect = self.image.get_rect()

        # start each new ship in the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Setting a decimal value for the ships position
        self.x = float(self.rect.x)

        # setting the movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ships position based on the movement flag"""
        if self.moving_right and (self.rect.right < self.screen_rect.right):
            self.x += self.settings.ship_speed
        if self.moving_left and (self.rect.left > 0):
            self.x -= self.settings.ship_speed

        # Update rect object from self.x
        self.rect.x = int(self.x)

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
    def center_ship2(self):
        """Place the ship2 next to ship on the screen"""
        # use lambda function to change the midbottom value of ship2 
        self.rect.midbottom = tuple(map(lambda i,j: i+j, self.screen_rect.midbottom, (100,0)))
        self.x = float(self.rect.x)