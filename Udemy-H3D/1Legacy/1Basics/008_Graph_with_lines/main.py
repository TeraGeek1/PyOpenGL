import sys, math
import numpy as np
import pygame as pg
from utils import *
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


pg.init()

screen_width , screen_height = 1600, 800
ortho_width, ortho_height = 4, 1.25
screen = pg.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pg.display.set_caption('Graphs in PyOpenGL')


def initOrtho():
    global ortho_width, ortho_height
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, ortho_width, -ortho_height, ortho_height)



def plot_line():
    global points

    glBegin(GL_LINE_STRIP)
    for p in points:
        glVertex2f(p[0], p[1])
    glEnd()



def create_points():
    global points
    px: GL_DOUBLE
    py: GL_DOUBLE

    for px in np.arange(0, ortho_width, 0.005):
        py = math.exp(-px) * math.cos(2 * math.pi * px)
        points.append((px, py))



initOrtho()
glLineWidth(3)

points = []
draw = False

create_points()

while True:

    pg.display.flip()

    for event in pg.event.get():

        if event.type == QUIT:
            pg.quit()
            sys.exit()
        
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    plot_line()

    # pg.time.wait(50)