import sys
import pygame as pg
from utils import *
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


pg.init()

screen_width , screen_height = 1600, 800
ortho_width, ortho_height = 640, 480
screen = pg.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pg.display.set_caption('Graphs in PyOpenGL')


def initOrtho():
    global ortho_width, ortho_height
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, ortho_width, 0, ortho_height)



def plot_point():
    global points
    glColor3f(1, 0, 0)
    glBegin(GL_POINTS)
    for p in points:
        glVertex2f(p[0], p[1])
    glEnd()



def plot_line():
    global lines, points
    
    for line in lines:
        glBegin(GL_LINE_STRIP)
        for p in line:
            glVertex2f(p[0], p[1])
        glEnd()

    glBegin(GL_LINE_STRIP)
    for p in points:
        glVertex2f(p[0], p[1])
    glEnd()



initOrtho()
glPointSize(5)

lines = []
points = []
draw = False

while True:

    pg.display.flip()

    for event in pg.event.get():

        if event.type == QUIT:
            pg.quit()
            sys.exit()

        elif event.type == MOUSEBUTTONDOWN:
            draw = True
            lines.append(points)
            points = []


        elif event.type == MOUSEBUTTONUP:
            draw = False


        if event.type == MOUSEMOTION and draw:
            p = pg.mouse.get_pos()
            x = map_value(0, screen_width,  0, ortho_width, p[0])
            y = map_value(0, screen_height, ortho_height, 0, p[1])
            points.append((x, y))
        
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    plot_line()

    # pg.time.wait(50)