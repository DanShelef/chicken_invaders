from Game import *

ID_TO_LOOP = {0: Loops.gameLoop}
    
def runGame():
    """
    """
    loopId = 0
    level = 1

    moveTargets = Levels.MOVE_TARGETS[level]

    ID_TO_ARGS = {0: ([Classes.OtherClasses.Target(level, i)
                       for i in xrange(Levels.TARGETS_COUNT[level])],
                      moveTargets,
                      Levels.MOVE_TARGETS_ARGS[level])}

    while True:
        if loopId not in ID_TO_LOOP:
            raise Exception("'loopId' is not in 'ID_TO_LOOP'")
        elif loopId in ID_TO_ARGS:
            loopId = ID_TO_LOOP[loopId](*ID_TO_ARGS[loopId])
        else:
            loopId = ID_TO_LOOP[loopId]()

runGame()
