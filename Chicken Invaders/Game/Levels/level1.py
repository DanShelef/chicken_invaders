import random, time
from Game.GeneralPygame import SCREEN_WIDTH
from Game.Etc import SPACESHIP_WIDTH, PICS_PATH, MEAT_BONUS, UPGRADE_BONUS

def moveTargets(targets, rays, stop, delta):
    """
    """
    wait = 10
    if stop:
        for target in targets:
            target.frameCounter = (target.frameCounter - 1) % wait
        if target.frameCounter is 0:
            stop = False
            delta *= -1
    else:
        for target in targets:
            target.frameCounter = wait
            stop = target.move(rays, stop, delta)

    return stop, delta

def moveFunction(target, rays, stop, delta):
    """
    """
    target.x += delta
    if not target.isAllIn():
        stop = True
    for ray in rays:
        ray.hitTarget(target)
    return stop



### Levels Constants:
ARGS = (False, 5)
LINE = 16
TARGETS_COUNT = LINE * 3
UPGRADES = TARGETS_COUNT

bonuses = [[MEAT_BONUS] for i in xrange(TARGETS_COUNT)]
for i in xrange(UPGRADES):
    bonuses[i] += [UPGRADE_BONUS]
random.seed(time.time())
random.shuffle(bonuses)

TARGETS_PICS            = {i:PICS_PATH + r"\Chicken.png"
                           for i in xrange(TARGETS_COUNT)}
TARGETS_WIDTHS          = {i:SPACESHIP_WIDTH
                           for i in xrange(TARGETS_COUNT)}
TARGETS_HEIGHTS         = {i:SPACESHIP_WIDTH
                           for i in xrange(TARGETS_COUNT)}
TARGETS_ANGLES          = {i:0
                           for i in xrange(TARGETS_COUNT)}
TARGETS_START_POSITION  = {i:((i % LINE + 1) * SPACESHIP_WIDTH,
                              (i / LINE + 1) * SPACESHIP_WIDTH)
                           for i in xrange(TARGETS_COUNT)}
TARGETS_MOVE_FUNCTION   = {i:[moveFunction]
                           for i in xrange(TARGETS_COUNT)}
TARGETS_HEALTH          = {i:30
                           for i in xrange(TARGETS_COUNT)}
TARGETS_VALUE           = {i:10
                           for i in xrange(TARGETS_COUNT)}
TARGETS_BONUSES         = {i:bonuses[i]
                           for i in xrange(TARGETS_COUNT)}