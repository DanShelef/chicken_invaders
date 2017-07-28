import random, time, math
from Game.GeneralPygame import SCREEN_WIDTH, move
from Game.Etc import SPACESHIP_WIDTH, PICS_PATH

SIZES = (1, 2, 3)
SIZE_TO_VELOCITY = {1:(10, 13),
                    2:(7, 10),
                    3:(5, 8)}

def moveTargets(targets, rays):
    """
    """
    move(targets, rays)
    return tuple()

def createMoveFunction(size):
    """
    """
    velocity = random.randrange(*(SIZE_TO_VELOCITY[size]))
    def moveFunction(target, rays):
        target.x += int(velocity * math.cos(math.radians(target.angle)))
        target.y += int(velocity * math.sin(math.radians(target.angle)))
        for ray in rays:
            ray.hitTarget(target)
    return moveFunction


TARGETS_PICS           = dict()
TARGETS_WIDTHS         = dict()
TARGETS_HEIGHTS        = dict()
TARGETS_ANGLES         = dict()
TARGETS_START_POSITION = dict()
TARGETS_MOVE_FUNCTION  = dict()
TARGETS_HEALTH         = dict()
TARGETS_VALUE          = dict()
TARGETS_BONUSES        = dict()

for i in xrange(TARGETS_COUNT):
    size = random.choice(SIZES)
    TARGETS_PICS           = {i:PICS_PATH + r"\Meteor.png"}
    TARGETS_WIDTHS         = {i:SPACESHIP_WIDTH * 0.4 * size}
    TARGETS_HEIGHTS        = {i:SPACESHIP_WIDTH * 0.4 * size}
    TARGETS_ANGLES         = {i: 225}
    TARGETS_START_POSITION = {i:(SCREEN_WIDTH)}
    TARGETS_MOVE_FUNCTION  = {i:createMoveFunction(size)}
    TARGETS_HEALTH         = {i:20 * size}
    TARGETS_VALUE          = {i:10}
    TARGETS_BONUSES        = {i:list()}