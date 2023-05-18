import math
import numpy as np
from random import choice, randint

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Utils import *

pygame.init()

screen_width = 800
screen_height = 800
ortho_left = 0
ortho_right = 800
ortho_top = 800
ortho_bottom = 0

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Polygons in PyOpenGL')


def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(ortho_left, ortho_right, ortho_top, ortho_bottom)


def plot_polygon():

    glBegin(GL_QUAD_STRIP)
    for p in points:
        glColor(p[2], p[3], p[4], 1)
        glVertex2f(p[0], p[1])
    glEnd()
    

glLineWidth(3)

done = False
init_ortho()
points = []
colors = [0.25, 0.5, 0.75, 1]

while not done:
    p = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == MOUSEBUTTONDOWN:
            points.append((randint(ortho_left -10, ortho_right + 10),
                           randint(ortho_bottom - 10, ortho_top + 10),
                           choice(colors), choice(colors), choice(colors))
            )
            points.append((randint(ortho_left -10, ortho_right + 10),
                           randint(ortho_bottom - 10, ortho_top + 10),
                           choice(colors), choice(colors), choice(colors))
            )


    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    plot_polygon()
    pygame.display.flip()
    print(len(points))
pygame.quit()
