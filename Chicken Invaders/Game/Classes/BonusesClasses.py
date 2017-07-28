from Game.Classes.OtherClasses import movingObj
from Game.Etc import *

class Upgrade(movingObj):
    """
    """
    def __init__(self, x, y, kind=None):
        """
        """
        if kind is None:
            kind = randomUpgrade()
        imagePath = KIND_TO_UPGRADE_PIC[kind]
        width = UPGRADE_SIZE
        height = UPGRADE_SIZE
        angle = 0
        super(Upgrade, self).__init__(imagePath, width, height, angle, x, y, [upgradeMovment])
        self.kind = kind


class Meat(movingObj):
    """
    """
    def __init__(self, x, y):
        """
        """
        self.score = randomScore()
        if self.score == BIG_CHICKEN:
            imagePath = PICS_PATH + r"\BigChicken.png"
            width = BIG_CHICKEN_SIZE
            height = BIG_CHICKEN_SIZE
        else:
            imagePath = PICS_PATH + r"\SmallChicken.png"
            width = SMALL_CHICKEN_SIZE
            height = SMALL_CHICKEN_SIZE
        angle = 0
        self.vx, self.vy = randomVelocity()
        super(Meat, self).__init__(imagePath, width, height, angle, x, y, [meatMovment])
        self.waitFrames = FPS * 3 / 4
        self.bouncesCounter = 0
