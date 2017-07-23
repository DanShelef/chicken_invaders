import pygame
from Game.GeneralPygame import *
from Game.Etc import *
from Game.Classes.LoopsClasses import Background, Spaceship

window, fpsClock = start(full_screen=True)
background = Background()
spaceship = Spaceship()

def gameLoop(targets, moveTargets, args):
    """
    """
    score = 0
    bullets = list()
    dangers = list()
    bonuses = list()
    while True:
        keys = pygame.key.get_pressed()
        spaceship.keyboardUpdate(keys[K_LEFT],
                                 keys[K_RIGHT],
                                 keys[K_UP],
                                 keys[K_DOWN],
                                 keys[K_f])
        if keys[K_F4] and (keys[K_LALT] or keys[K_RALT]):
            exit()
        if spaceship.lives is 0:
            exit()

        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_f:
                    bullets += spaceship.shoot()
            elif event.type == MOUSEBUTTONUP:
                spaceship.flickeringFrames = FLICKERING_FRAMES

        move([background, spaceship] + bullets + dangers + bonuses)
        args = moveTargets(targets, spaceship.rays, *args)

        bullets += spaceship.autoShoot()

        raysDamage(spaceship)
        bulletsDamage(bullets, targets)
        score += targetsCheck(spaceship, targets, bonuses)

        #Drawing order:
        background.draw(window)
        draw(window, bullets)
        spaceship.draw(window)
        draw(window, dangers + targets + bonuses)
        pygame.display.update((0,0,SCREEN_WIDTH,SCREEN_HEIGHT))

        #print "score ",score

        fpsClock.tick(FPS)