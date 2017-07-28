from Game.Exceptions import WeirdBonus
from Game.Classes.BonusesClasses import Upgrade, Meat

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
        if isinstance(bonuses[i], Upgrade) and bonuses[i].isAllOut():
            bonuses.remove(bonuses[i])
            i -= 1
        elif isinstance(bonuses[i], Meat) and bonuses[i].waitFrames is 0:
            bonuses.remove(bonuses[i])
            i -= 1
        elif bonuses[i].isColiding(spaceship):
            if isinstance(bonuses[i], Upgrade):
                spaceship.upgrade(bonuses[i].kind)
            elif isinstance(bonuses[i], Meat):
                score += bonuses[i].score
            else:
                raise WeirdBonus("Unknown bonus type!")
            bonuses.remove(bonuses[i])
            i -= 1
        i += 1

    return score