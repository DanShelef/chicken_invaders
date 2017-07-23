import random, pygame
from pygame import transform
from pygame.image import load
from Game.GeneralPygame import *
from Game.Etc import *
from Game.Levels import TARGETS_COUNT, TARGETS_PICS, TARGETS_WIDTHS, TARGETS_HEIGHTS, TARGETS_ANGLES, TARGETS_START_POSITION, TARGETS_MOVE_FUNCTION, TARGETS_HEALTH, TARGETS_VALUE, TARGETS_BONUSES


### Classes:
class movingObj(object):
    """
    """
    def __init__(self, imagePath, width, height, angle, x, y, moveFunction):
        """
        """
        self.image = load(imagePath)
        self.width = width
        self.height = height
        self.angle = angle
        self.x = x
        self.y = y
        self.moveFunction = moveFunction

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
        return self.moveFunction(self, *args)

    def isColiding(self, obj):
        """
        """
        return (abs(self.y - obj.y) < (self.height + obj.height) / 2) \
               and (abs(self.x - obj.x) < (self.width + obj.width) / 2)

    def isAllOut(self):
        """
        """
        return (self.x < 0 - self.width / 2)\
               or (self.x < SCREEN_WIDTH + self.width / 2)\
               or (self.y < 0 - self.height / 2)\
               or (self.y < SCREEN_HEIGHT + self.height / 2)\


class Upgrade(movingObj):
    """
    """
    pass

class Danger(movingObj):
    """
    """
    def __init__(self, imagePath, width, height, angle, x, y, moveFunction):
        """
        """
        super(Danger, self).__init__(imagePath, width, height, angle, x, y, moveFunction)
        self.framesCounter = 0

    def isAllIn(self):
        """
        """
        return (0 + self.height / 2 <= self.y <= SCREEN_HEIGHT - self.height / 2)\
               and (0 + self.width / 2 <= self.x <= SCREEN_WIDTH - self.width / 2)

class Target(Danger):
    """
    """
    def __init__(self, level, targetId):
        imagePath = TARGETS_PICS[level][targetId]
        width = TARGETS_WIDTHS[level][targetId]
        height = TARGETS_HEIGHTS[level][targetId]
        angle = TARGETS_ANGLES[level][targetId]
        x, y = TARGETS_START_POSITION[level][targetId]
        moveFunction = TARGETS_MOVE_FUNCTION[level][targetId]
        super(Target, self).__init__(imagePath, width, height, angle, x, y, moveFunction)
        self.hp = TARGETS_HEALTH[level][targetId]
        self.score = TARGETS_VALUE[level][targetId]
        self.bonuses = TARGETS_BONUSES[level][targetId]



def targetMovment(target, spaceship):
    """
    """
    if IS_WEAPON_RAY[spaceship.weaponKind]\
       and spaceship.autoShootActive:
        target.isHit(spaceship.ray)