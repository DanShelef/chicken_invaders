import random, pygame
from pygame import transform
from pygame.image import load
from Game.GeneralPygame import *
from Game.Etc import *

### Classes:
class movingObj(object):
    """
    """
    def __init__(self, imagePath, width, height, angle, x, y, moveFunctions):
        """
        """
        self.image = load(imagePath)
        self.width = width
        self.height = height
        self.angle = angle
        self.x = x
        self.y = y
        self.moveFunctions = moveFunctions
        self.currentMovment = 0

    def draw(self, window):
        """
        Doc:        Drawing the shot
        Arguments:  window (Surface obj.) - The surface to draw the shots on
        Returns:    None
        """
        image = transform.scale(self.image, (self.width, self.height))
        image = transform.rotate(image, self.angle)
        window.blit(image, (self.x - image.get_width() / 2, self.y - image.get_height() / 2))

    def move(self, *args):
        """
        """
        return self.moveFunctions[self.currentMovment](self, *args)

    def isColiding(self, obj):
        """
        """
        return (abs(self.y - obj.y) < (self.height + obj.height) / 2) \
               and (abs(self.x - obj.x) < (self.width + obj.width) / 2)

    def isAllOut(self):
        """
        """
        return (self.x < 0 - self.width / 2)\
               or (self.x > SCREEN_WIDTH + self.width / 2)\
               or (self.y < 0 - self.height / 2)\
               or (self.y > SCREEN_HEIGHT + self.height / 2)\
