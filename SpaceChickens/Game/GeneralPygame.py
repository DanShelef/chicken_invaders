### Imports:
import pygame, sys, os, time, numpy
from pygame.locals import *
from win32api import GetSystemMetrics

### Constants:
SCREEN_WIDTH = GetSystemMetrics(0)
SCREEN_HEIGHT = GetSystemMetrics(1)

#       colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
AZURE = (0, 127, 255)
SILVER = (200, 200, 200)

color = (50, 100, 100)


# Functions:
def exit():
    pygame.quit()
    sys.exit()

def start(width=0, height=0, create_clock=True, full_screen=False):
    x = (SCREEN_WIDTH - width) / 2
    y = (SCREEN_HEIGHT - height) / 2
    if full_screen:
        x = 0
        y = 0
        width = SCREEN_WIDTH
        height = SCREEN_HEIGHT
    os.environ['SDL_VIDEO_WINDOW_POS'] = "{0}, {1}".format(x, y)
    pygame.init()
    window = pygame.display.set_mode((width, height),
                                     HWSURFACE|DOUBLEBUF|RESIZABLE)
    if create_clock:
        fpsClock = pygame.time.Clock()
        return window, fpsClock
    return window

def draw(window, objects, *args):
    for shape in objects:
        shape.draw(window, *args)

def move(objects, *args):
    for shape in objects:
        shape.move(*args)

def write_text():
    pass

def move_rects():
    pass

def grow_rect():
    pass

def centerToCorner(obj):
    x, y = obj.position
    x -= obj.width / 2
    y -= obj.height / 2
    return x, y

def changeAlpha(image, alpha=255):
    if alpha < 1:
        alpha = 1
    elif alpha > 255:
        alpha = 255
    imageAlpha = pygame.surfarray.pixels_alpha(image)
    newImageAlpha = numpy.minimum(imageAlpha, numpy.ones(imageAlpha.shape, dtype=imageAlpha.dtype)) * alpha
    numpy.copyto(imageAlpha, newImageAlpha)
    del imageAlpha

"""
#1
L_SQUIR_IMG = pygame.image.load('squirrel.png')
R_SQUIR_IMG = pygame.transform.flip(L_SQUIR_IMG, True, False)


#2
window = pygame.display.set_mode((width, height),
                                 HWSURFACE|DOUBLEBUF|RESIZABLE)
while True:
    for event in pygame.event.get():
        if event.type == VIDEORESIZE:
            window = pygame.display.set_mode(event.size,
                                             HWSURFACE|DOUBLEBUF|RESIZABLE)
            pygame.display.flip()
            WINDOW_WIDTH = window.get_width()
            WINDOW_HEIGHT = window.get_height()
"""


if __name__ == "__main__":
    window, fpsClock = start(400, 300)
    window.fill(color)
    pygame.display.set_caption('Hello World!')
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        pygame.display.update()