import math
from pygame import transform
from pygame.image import load
from Game.GeneralPygame import *
from Game.Etc import *
from Game.Classes.OtherClasses import movingObj

class Bullet(movingObj):
    """
    Representing a single independent shot, a bullet
    """
    def __init__(self, kind, damage, x, y):
        """
        Arguments:  kind (int) - The kind of the weapon, see Etc.py for more information
                    damage (int) - Amount of the damage the bullet can make
                    x (int) - X coordinate of the bullet
                    y (int) - Y coordinate of the bullet
        """
        imagePath = KIND_TO_PIC[kind]
        width = int((SPACESHIP_WIDTH * damage) / 100.0)
        height = int((SPACESHIP_WIDTH * damage) / 35.0)
        angle = 0
        super(Bullet, self).__init__(imagePath, width, height, angle, x, y, bulletMovment)
        self.v = KIND_TO_VELOCITY[kind]
        self.DAMAGE = damage

    def tilt(self, angle_change):
        """
        Doc:        Changing the angle of the bullet by given value
        Arguments:  angle_change (int) - the change in the bullet's angle
        Returns:    None
        """
        self.angle += angle_change


class Ray(object):
    """
    """
    def __init__(self, spaceship, damage):
        """
        """
        self.damage = damage
        self.image = load(KIND_TO_PIC[spaceship.weaponKind])
        self.width = int(SPACESHIP_WIDTH * self.damage / 100.0)
        self.heights = [SCREEN_HEIGHT]
        self.x = spaceship.x - self.width / 2
        self.y = spaceship.y
        self.spaceship = spaceship
        self.target = None

    def draw(self, window):
        """
        """
        image = transform.scale(self.image, (self.width, self.heights[0]))
        window.blit(image, (self.x, self.y - self.heights[0]))

    def move(self):
        self.x = self.spaceship.x - self.width / 2
        self.y = self.spaceship.y

    def hitTarget(self, target):
        """
        """
        if abs(self.x - target.x) > (self.width + target.width) / 2:
            return
        height = self.y - target.y
        if height < 0:
            return
        self.heights.append(height)
        self.heights.sort()
        if height == self.heights[0]:
            self.target = target
            return
