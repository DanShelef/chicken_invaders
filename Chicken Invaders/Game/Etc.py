### Imports:
import math
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
#       Weapons
JOKER = 0
RED_WEAPON = 1
GREEN_WEAPON = 2
YELLOW_WEAPON = 3
RED_LEVEL_TO_DAMAGE    = {0:(10,),
                          1:(10,) * 2,
                          2:(10,) * 3,
                          3:(10,) * 4,
                          4:(10,) * 5,
                          5:(10,) * 6,
                          6:(10,) * 7,
                          7:(10,) * 8,}
GREEN_LEVEL_TO_DAMAGE  = {0:(10,),
                          1:(20,),
                          2:(15, 15),
                          3:(20, 20),
                          4:(15, 20, 15),
                          5:(15, 30, 15),
                          6:(15, 20, 20, 15),
                          7:(20, 20, 20, 20)}
YELLOW_LEVEL_TO_DAMAGE = {0:(10,),
                          1:(20,),
                          2:(30,),
                          3:(40,),
                          4:(50,),
                          5:(60,),
                          6:(70,),
                          7:(80,)}
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

def bulletsDamage(bullets, targets):
    """
    """
    i = 0
    j = 0
    while i < len(bullets):
        if bullets[i].isAllOut():
            bullets.remove(bullets[i])
            i -= 1
        else:
            j = 0
            while (j < len(targets)) and len(bullets):
                if targets[j].isAllOut():
                    pass
                elif targets[j].isColiding(bullets[i]) and targets[j].hp > 0:
                    targets[j].hp -= bullets[i].DAMAGE
                    bullets.remove(bullets[i])
                    i -= 1
                    j = len(targets)
                j += 1
        i += 1

def raysDamage(spaceship):
    """
    """
    for ray in spaceship.rays:
        if ray.target is not None:
            if (ray.target is not None) and (spaceship.framesFromShot is 1):
                ray.target.hp -= ray.damage
            if ray.target.hp <= 0:
                ray.target = None
                ray.heights.remove(ray.heights[0])

def targetsCheck(spaceship, targets, bonuses):
    """
    """
    i = 0
    score = 0

    while i < len(targets):
        if targets[i].isColiding(spaceship) and (spaceship.flickeringFrames is 0):
            spaceship.lives -= 1
            spaceship.flickeringFrames = FLICKERING_FRAMES
        if targets[i].hp <= 0:
            bonuses += targets[i].getBonuses()
            score += targets[i].score
            targets.remove(targets[i])
            i -= 1
        i += 1
    return score

def bonusesCheck(spaceship, bonuses):
    """
    """
    i = 0
    score = 0

    while i < len(bonuses):
        if bonuses[i].isAllOut():
            bonuses.remove(bonuses[i])
            i -= 1
        elif bonuses[i].isColiding(spaceship):
            if isinstance(bonuses[i], Upgrade):
                spaceship.upgrade(bonuses[i].kind)
            elif isinstance(bonuses[i], Meat):
                score += bonuses[i].score
            else:
                raise Exception("Unknown bonus type!")
            bonuses.remove(bonuses[i])
            i -= 1
        i += 1

    return score
