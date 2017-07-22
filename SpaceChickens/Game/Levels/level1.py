from GeneralPygame import SCREEN_WIDTH
from Game.Etc import SPACESHIP_WIDTH, PICS_PATH


isOut = False
wait = 10

def moveFunction(target, rays):
    """
    delta = 7
    x = target.x
    if not (0 + target.width / 2 < target.x < SCREEN_WIDTH - target.width / 2)\
       and target.frameCounter == 0:
        isOut = True
        target.frameCounter += wait
        return
    elif not (0 + target.width / 2 < target.x < SCREEN_WIDTH - target.width / 2)\
       and target.frameCounter == 1:

    if LEFT:
        delta *= -1
    """
    for ray in rays:
        ray.hitTarget(target)

TARGETS_COUNT1 = 10

TARGETS_PICS1            = {i:PICS_PATH + r"\Chicken.png"
                            for i in xrange(TARGETS_COUNT1)}
TARGETS_WIDTHS1          = {i:SPACESHIP_WIDTH
                            for i in xrange(TARGETS_COUNT1)}
TARGETS_HEIGHTS1         = {i:SPACESHIP_WIDTH
                            for i in xrange(TARGETS_COUNT1)}
TARGETS_ANGLES1          = {i:0
                            for i in xrange(TARGETS_COUNT1)}
TARGETS_START_POSITION1  = {i:(int((i+1) * SPACESHIP_WIDTH * 1.5), 100)
                            for i in xrange(TARGETS_COUNT1)}
TARGETS_MOVE_FUNCTION1   = {i:moveFunction
                            for i in xrange(TARGETS_COUNT1)}
TARGETS_HEALTH1          = {i:1
                            for i in xrange(TARGETS_COUNT1)}
TARGETS_VALUE1           = {i:10
                            for i in xrange(TARGETS_COUNT1)}
TARGETS_BONUSES1         = {i:list()
                            for i in xrange(TARGETS_COUNT1)}