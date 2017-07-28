import random, time
from Game.GeneralPygame import *
from Game.Classes.OtherClasses import movingObj
from Game.Levels import TARGETS_PICS, TARGETS_WIDTHS, TARGETS_HEIGHTS, TARGETS_ANGLES, TARGETS_START_POSITION
from Game.Levels import TARGETS_MOVE_FUNCTION, TARGETS_HEALTH, TARGETS_VALUE, TARGETS_BONUSES

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

    def getBonuses(self):
        """
        """
        newBonuses = list()
        for bonus in self.bonuses:
            newBonuses.append(bonus(target=self))
        return newBonuses
