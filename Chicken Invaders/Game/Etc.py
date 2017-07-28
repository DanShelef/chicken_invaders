### Imports:
import math, random, time
from Game.GeneralPygame import SCREEN_WIDTH, SCREEN_HEIGHT

### Constants:
WINDOW_CAPTION = "Chicken Invaders"
FPS = 24
SPACESHIP_WIDTH = int(SCREEN_WIDTH * 0.05)
SPACESHIP_HEIGHT = int(SCREEN_WIDTH * 0.04)
UPGRADE_SIZE = int(SPACESHIP_WIDTH * 0.2)
FRAMES_BETWEEN_SHOTS = FPS / 3
FLICKERING_FRAMES = int(FPS * 2.5)
PICS_PATH = r"Chicken Invaders\Game\Pictures"
BIG_CHICKEN = 100
SCORE_OPTIONS = (10, 20, 30, 40, 50, BIG_CHICKEN)
BIG_CHICKEN_SIZE = SPACESHIP_WIDTH * 3 / 4
SMALL_CHICKEN_SIZE = SPACESHIP_WIDTH * 2 / 3
GRAVITY = 5
MEAT_BONUS = 0
UPGRADE_BONUS = 1

#       Weapons
WEAPONS_AMOUNT = 3
WEAPONS_LEVELS_AMOUNT = 8
JOKER = 0
RED_WEAPON = 1
GREEN_WEAPON = 2
YELLOW_WEAPON = 3
RED_LEVEL_TO_DAMAGE    = {i:(10,) * (i + 1)
                          for i in xrange(WEAPONS_LEVELS_AMOUNT)}
GREEN_LEVEL_TO_DAMAGE  = {0:(10,),
                          1:(20,),
                          2:(15, 15),
                          3:(20, 20),
                          4:(15, 20, 15),
                          5:(15, 30, 15),
                          6:(15, 20, 20, 15),
                          7:(20, 20, 20, 20)}
YELLOW_LEVEL_TO_DAMAGE = {i:(10 * (i + 1),)
                          for i in xrange(WEAPONS_LEVELS_AMOUNT)}
KIND_TO_DAMAGE = {RED_WEAPON   : RED_LEVEL_TO_DAMAGE,
                  GREEN_WEAPON : GREEN_LEVEL_TO_DAMAGE,
                  YELLOW_WEAPON: YELLOW_LEVEL_TO_DAMAGE}

KIND_TO_VELOCITY = {RED_WEAPON   : -25,
                    GREEN_WEAPON : -20,
                    YELLOW_WEAPON: 0}
KIND_TO_SHOT_PIC = {RED_WEAPON   : PICS_PATH + r"\Red.png",
                    GREEN_WEAPON : PICS_PATH + r"\Green.png",
                    YELLOW_WEAPON: PICS_PATH + r"\Yellow.png"}
IS_WEAPON_RAY = {RED_WEAPON   : False,
                 GREEN_WEAPON : False,
                 YELLOW_WEAPON: True}

KIND_TO_UPGRADE_PIC = {JOKER        : PICS_PATH + r"\JokerUpgrade.png",
                       RED_WEAPON   : PICS_PATH + r"\RedUpgrade.png",
                       GREEN_WEAPON : PICS_PATH + r"\GreenUpgrade.png",
                       YELLOW_WEAPON: PICS_PATH + r"\YellowUpgrade.png"}

### Functions:
def bulletMovment(bullet):
    """
    """
    bullet.x += bullet.v * math.sin(math.radians(bullet.angle))
    bullet.y += bullet.v * math.cos(math.radians(bullet.angle))

def upgradeMovment(upgrade):
    """
    """
    upgrade.angle += 10
    upgrade.y += 5

def meatMovment(meat):
    """
    """
    meat.x += meat.vx
    meat.y += meat.vy
    meat.vy += GRAVITY
    if meat.x < meat.width / 2:
        meat.x  = meat.width / 2
        meat.vx = -meat.vx
    elif meat.x > SCREEN_WIDTH - meat.width / 2:
        meat.x = SCREEN_WIDTH - meat.width / 2
        meat.vx = -meat.vx
    if meat.y > SCREEN_HEIGHT - meat.width / 2:
        meat.y = SCREEN_HEIGHT - meat.width / 2
        meat.vy = -meat.vy / 2
        meat.bouncesCounter += 1
        if meat.bouncesCounter > 3:
            meat.vy = 0
            meat.vx = 0
            meat.waitFrames -= 1

def randomUpgrade():
    """
    """
    jokerChance = 0.1
    random.seed(time.time())
    kind = random.random()
    for weaponKind in xrange(1, WEAPONS_AMOUNT + 1):
        if kind < (1 - jokerChance) / WEAPONS_AMOUNT * weaponKind:
            return weaponKind
    return JOKER

def randomScore():
    """
    """
    random.seed(time.time())
    return random.choice(SCORE_OPTIONS)

def randomVelocity():
    """
    """
    angleRange = (60, 120)
    velocityRange = (30, 50)
    random.seed(time.time())
    angle = random.randint(*angleRange)
    velocity = random.randint(*velocityRange)
    vx = velocity * math.cos(math.radians(angle))
    vy = velocity * math.sin(math.radians(angle))
    return vx, -vy