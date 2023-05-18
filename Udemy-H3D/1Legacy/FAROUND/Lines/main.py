import sys
import pygame as pg
from random import choice, randint
from utils import *
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


pg.init()

screen_width , screen_height = 1000, 800
ortho_width, ortho_height = 640, 480
screen = pg.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pg.display.set_caption('Graphs in PyOpenGL')



points = []
mouse_down = False
stop = False
max_points = 15
colors = [0, 0.75, 1]


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
        glColor3f(p[2], p[3], p[4])
        glVertex2f(p[0], p[1])
    glEnd()


def plot_lines():
    global points
    glBegin(GL_LINE_STRIP)
    # glBegin(GL_LINE_LOOP)
    for p in points:
        glColor3f(p[2], p[3], p[4])
        glVertex2f(p[0], p[1])
    glEnd()


def create_Point():
    if len(points) > max_points:
        for i in range(0, (len(points) - max_points)):
            points.remove(points[i])
    
    x = randint(0, ortho_width)
    y = randint(0, ortho_height)
    r, g, b = 0, 0, 0
    while (r + g + b) <= 1.5 or (r + g + b) >= 3:
        r = choice(colors)
        g = choice(colors)
        b = choice(colors)
    points.append((x, y, r, g, b))


initOrtho()
glPointSize(3)

while True:

    pg.display.flip()

    for event in pg.event.get():

        if event.type == QUIT:
            pg.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
                stop = True
        
        while stop:
            for event in pg.event.get():
                if event.type == MOUSEBUTTONUP:
                    stop = False
        
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    create_Point()
    plot_lines()
    # plot_point()

    pg.time.wait(100)
