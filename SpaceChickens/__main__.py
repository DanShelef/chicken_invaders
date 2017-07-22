from Game import *

ID_TO_LOOP = {0: Loops.gameLoop}
    
def runGame():
    """
    """
    loopId = 0
    level = 1

    background = Loops.Background()
    spaceship = Loops.Spaceship()
    bullets = list()
    dangers = list()
    targets = [Classes.OtherClasses.Target(level, i)
               for i in xrange(Levels.TARGETS_COUNT[level])]
    bonuses = list()

    ID_TO_ARGS = {0: (bullets,
                      dangers,
                      targets,
                      bonuses)}

    while True:
        if loopId not in ID_TO_LOOP:
            raise Exception("'loopId' is not in 'ID_TO_LOOP'")
        elif loopId in ID_TO_ARGS:
            loopId = ID_TO_LOOP[loopId](*ID_TO_ARGS[loopId])
        else:
            loopId = ID_TO_LOOP[loopId]()

runGame()
