import pygame
from Game.GeneralPygame import *
from Game.Etc import *
from Game.Classes.LoopsClasses import Background, Spaceship

AMOUNT_OF_RAYS = 3
STARTING_RAY_INDEX = 1

window, fpsClock = start(full_screen=True)
background = Background()
spaceship = Spaceship()

def gameLoop(bullets,
             dangers,
             targets,
             bonuses):
    score = 0
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

                elif event.key == K_LEFTBRACKET:
                    spaceship.weaponKind = (spaceship.weaponKind % AMOUNT_OF_RAYS) + 1

                elif event.key == K_RIGHTBRACKET:
                    if spaceship.weaponKind == 1:
                        spaceship.weaponKind = 3

                    else:
                        spaceship.weaponKind -= 1

                elif event.key == K_9:
                    spaceship.weaponLevel = (spaceship.weaponLevel + 1) % 8

                elif event.key == K_0:
                    spaceship.weaponLevel = (spaceship.weaponLevel - 1) % 8

            elif event.type == MOUSEBUTTONUP:
                spaceship.flickeringFrames = FLICKERING_FRAMES



        move([background, spaceship] + bullets + dangers + bonuses)
        move(targets, spaceship.rays)

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