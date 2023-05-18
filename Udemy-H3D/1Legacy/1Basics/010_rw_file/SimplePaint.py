import math
import numpy as np
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from utils import *

pygame.init()

screen_width = 800
screen_height = 800
ortho_left = -400
ortho_right = 400
ortho_top = -400
ortho_bottom = 400

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Simple Paint by TeraGeek')


def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(ortho_left, ortho_right, ortho_top, ortho_bottom)


def plot_point():
    glBegin(GL_POINTS)
    for p in lines:
        glVertex2f(p[0], p[1])
    glEnd()


def plot_graph():
    glBegin(GL_LINE_STRIP)
    px: GL_DOUBLE
    py: GL_DOUBLE
    for px in np.arange(0, 4, 0.005):
        py = math.exp(-px) * math.cos(2 * math.pi * px)
        glVertex2f(px, py)
    glEnd()


def plot_lines():
    for l in lines:
        glBegin(GL_LINE_STRIP)
        for coords in l:
            glVertex2f(coords[0], coords[1])
        glEnd()



def load_drawing():
    if os.path.exists(path):
        f = open(path, "r")
        num_lines = int(f.readline())
        global lines, points
        lines = []

        for l in range(num_lines):
            points = []
            lines.append(points)
            num_points = int(f.readline())
            for p in range(num_points):
                px, py = [float(value) for value in next(f).split()]
                points.append((px, py))

        f.close()
        print("Loaded file")
    else:
        print("There is no file to load!")



def save_drawing():
    f = open(path, 'w') 
    f.write(str(len(lines)) + "\n")
    for l in lines:
        f.write(str(len(l)) + "\n")
        for p in l:
            f.write(str(p[0]) + " " + str(p[1]) + "\n")

    f.close()
    print("File saved!")


def undo_line():
    if len(lines) > 0:
        redos.append(lines.pop(-1))

        if len(redos) >= 20:
            for p in range(len(redos) - 20):
                redos.remove(redos[-1])

            print("Undo")
        else:
            print("There is nothing to undo?")


def redo_line():
    if len(redos) > 0:
        lines.append(redos.pop(-1))


def clear_drawing():
    global lines, points, redos
    redos = []
    lines = []
    points = []


done = False
path = "drawing.txt"
Create_readme()
init_ortho()
glPointSize(5)
lines = []
points = []
redos = []
mouse_down = False


while not done:
    p = None
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True

        elif event.type == KEYDOWN:

            if event.key == K_s: # Save
                save_drawing()

            elif event.key == K_a: # Load
                load_drawing()
            
            elif event.key == K_d: # Undo
                undo_line()

            elif event.key == K_f: # Redo
                redo_line()

            elif event.key == K_SPACE:
                clear_drawing()

        elif event.type == MOUSEBUTTONDOWN:
            mouse_down = True
            points = []
            lines.append(points)

        elif event.type == MOUSEBUTTONUP:
            mouse_down = False

        elif event.type == MOUSEMOTION and mouse_down:
            p = pygame.mouse.get_pos()
            points.append((map_value(0, screen_width, ortho_left, ortho_right, p[0]),
                           map_value(0, screen_height, ortho_bottom, ortho_top, p[1])))


    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    plot_lines()
    pygame.display.flip()
    # pygame.time.wait(100)
pygame.quit()
