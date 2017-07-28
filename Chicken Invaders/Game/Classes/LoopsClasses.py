from pygame import transform
from pygame.image import load
from Game.GeneralPygame import *
from Game.Etc import *
from Game.Classes.WeaponRelated import Bullet, Ray

class Background(object):
    """
    Wraps anything related to the background
    """
    def __init__(self):
        """
        Arguments:  None
        """
        image = load(PICS_PATH + r"\space.jpg")
        self.IMAGE = transform.scale(image,
                                      (SCREEN_WIDTH, image.get_height()))
        self.HEIGHT = self.IMAGE.get_height()
        self.IMAGES_COUNT = SCREEN_HEIGHT / self.HEIGHT + 2
        self.v = 45
        self.x = [0 for i in xrange(self.IMAGES_COUNT)]
        self.y = [SCREEN_HEIGHT - self.HEIGHT * (i + 1)
                  for i in xrange(self.IMAGES_COUNT)]
        self.isFlipped = [i % 2 == 0 for i in xrange(self.IMAGES_COUNT)]

    def draw(self, window):
        """
        Doc:        Drawing the Background
        Arguments:  window (Surface obj.) - The surface to draw the background on
        Returns:    None
        """
        for i in xrange(self.IMAGES_COUNT):
            if self.y[i] + self.HEIGHT > 0:
                image = transform.flip(self.IMAGE, self.isFlipped[i], self.isFlipped[i])
                window.blit(image, (int(self.x[i]), int(self.y[i])))

    def move(self):
        """
        Doc:        Moving the background verticaly, for effects
        Arguments:  None
        Returns:    None
        """
        for i in xrange(self.IMAGES_COUNT):
            self.y[i] += float(self.v) / FPS

        if self.y[0] > SCREEN_HEIGHT:
            self.y.remove(self.y[0])
            self.y.append(self.y[-1] - self.HEIGHT)
            self.isFlipped.remove(self.isFlipped[0])
            self.isFlipped.append(not self.isFlipped[-1])


class Spaceship(object):
    """
    Representing the spaceship of the player
    """
    def __init__(self):
        """
        Arguments:  None
        """
        self.MAX_ANGLE = 21
        self.ROTATION = 3
        self.DELTA = 10
        self.width = SPACESHIP_WIDTH
        self.height = SPACESHIP_HEIGHT
        self.IMAGE = transform.scale(load(PICS_PATH + r"\smallSpaceship.png"),
                                      (self.width, self.height))
        self.angle = 0
        self.x = (SCREEN_WIDTH - self.width) / 2
        self.y = SCREEN_HEIGHT - self.height
        self.rightIsPressed = False
        self.leftIsPressed = False
        self.downIsPressed = False
        self.upIsPressed = False
        self.weaponKind = RED_WEAPON
        self.weaponLevel = 0
        self.autoShootActive = False
        self.framesFromShot = 0
        self.rays = list()
        self.lives = 3
        self.flickeringFrames = 0

    def draw(self, window):
        """
        Doc:        Drawing the Spaceship
        Arguments:  window (Surface obj.) - The surface to draw the spaceship on
        Returns:    None
        """
        image = transform.rotate(self.IMAGE, self.angle)
        if self.flickeringFrames % (FPS / 2) > self.flickeringFrames % (FPS / 4):
            changeAlpha(image, 100)
        if self.flickeringFrames:
            self.flickeringFrames -= 1
        if IS_WEAPON_RAY[self.weaponKind] and self.autoShootActive:
            draw(window, self.rays)
        window.blit(image, (self.x - self.width / 2, self.y - self.height / 2))

    def move(self):
        """
        Doc:        Moving the spaceship on the screen
        Arguments:  None
        Returns:    None
        """
        if self.upIsPressed and not self.downIsPressed:
            self.y -= self.DELTA
            if self.y < self.height / 2:
                self.y = self.height / 2
        elif self.downIsPressed and not self.upIsPressed:
            self.y += self.DELTA
            if self.y > SCREEN_HEIGHT - self.height / 2:
                self.y = SCREEN_HEIGHT - self.height / 2

        if self.leftIsPressed and not self.rightIsPressed:
            self.x -= self.DELTA
            if self.x < self.width / 2:
                self.x = self.width / 2
            if self.angle < self.MAX_ANGLE:
                self.angle += self.ROTATION
        elif self.rightIsPressed and not self.leftIsPressed:
            self.x += self.DELTA
            if self.x > SCREEN_WIDTH - self.width / 2:
                self.x = SCREEN_WIDTH - self.width / 2
            if self.angle > -self.MAX_ANGLE:
                self.angle -= self.ROTATION
        else:
            if self.angle > 0:
                self.angle -= self.ROTATION
            elif self.angle < 0:
                self.angle += self.ROTATION

        if self.rays:
            move(self.rays)
    
    def shoot(self):
        """
        Doc:        Shooting according to the spaceship weapon
        Arguments:  None
        Returns:    The bullets fired (list[Bullet obj.])
        """
        damage = KIND_TO_DAMAGE[self.weaponKind][self.weaponLevel]
        bullets_count = len(damage)
        self.rays = list()
        if IS_WEAPON_RAY[self.weaponKind]:
            bullets = list()
            rays = KIND_TO_DAMAGE[self.weaponKind][self.weaponLevel]
            for damage in rays:
                self.rays.append(Ray(self, damage))
        else:
            tilt_count = bullets_count - bullets_count / 2 - 1
            tilt_angle = 15
            bullets = [Bullet(self.weaponKind, damage[i], self.x, self.y) for i in xrange(bullets_count)]
            i = 0
            while i < tilt_count:
                bullets[i].tilt(tilt_angle * (i + 1))
                bullets[-i - 1].tilt(-tilt_angle * (i + 1))
                i += 1
            bullets[i].x += 20
            bullets[-i - 1].x -= 20
        return bullets

    def autoShoot(self):
        """
        Doc:        Shooting every few frames if the player presses continuously on the shooting button
        Arguments:  None
        Returns:    Any new shots that has been made (list[Shot obj.])
        """
        if self.autoShootActive:
            if self.framesFromShot == FRAMES_BETWEEN_SHOTS:
                self.framesFromShot = 0
                return self.shoot()
            self.framesFromShot += 1
        else:
            self.framesFromShot = 0
            self.rays = list()
        return list()

    def keyboardUpdate(self, left, right, up, down, fire):
        """
        Doc:        Updating boolians in the object which depends on the keyboard
        Arguments:  left (bool) - State of the left moving key (pressed/not pressed)
                    right (bool) - State of the right moving key (pressed/not pressed)
                    up (bool) - State of the up moving key (pressed/not pressed)
                    down (bool) - State of the down moving key (pressed/not pressed)
                    fire (bool) - State of the fire key (pressed/not pressed)
        Returns:    None
        """
        self.leftIsPressed = left
        self.rightIsPressed = right
        self.upIsPressed = up
        self.downIsPressed = down
        self.autoShootActive = fire

        self.rays = list()
        if self.autoShootActive and IS_WEAPON_RAY[self.weaponKind]:
            rays = KIND_TO_DAMAGE[self.weaponKind][self.weaponLevel]
            for damage in rays:
                self.rays.append(Ray(self, damage))

    def upgrade(self, upgrade):
        if (upgrade is JOKER) or (upgrade is self.weaponKind):
            self.weaponLevel += 1
            self.weaponLevel -= self.weaponLevel / WEAPONS_LEVELS_AMOUNT
        else:
            self.weaponKind = upgrade
            self.weaponLevel = 0