import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Cube import *
from LoadMesh import *

pygame.init()

# project settings
screen_width = 1000
screen_height = 800
background_color = (0, 0, 0, 1)
drawing_color = (1, 1, 1, 1)

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption("OpenGL in Python")

cube = Cube(GL_LINE_LOOP)
mesh = LoadMesh(
    "Udemy-H3D/1Legacy/1Basics/019_engine_simple_load/obj/cube.obj", GL_LINE_LOOP
)


def initialise():
    glClearColor(
        background_color[0],
        background_color[1],
        background_color[2],
        background_color[3],
    )
    glColor(drawing_color)

    # projection
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, (screen_width / screen_height), 0.1, 1000.0)

    # modelview
    glMatrixMode(GL_MODELVIEW)
    glTranslate(0, 0, -5)
    glLoadIdentity()
    glViewport(0, 0, screen.get_width(), screen.get_height())
    glEnable(GL_DEPTH_TEST)
    glTranslate(0, 0, -4)


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glRotatef(1, 10, 10, 10)
    glPushMatrix()
    # cube.draw()
    mesh.draw()
    glPopMatrix()


cycle = 1
done = False
initialise()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                cycle = cycle * -1

                if cycle == 1:
                    mesh.draw_type = GL_LINE_LOOP

                else:
                    mesh.draw_type = GL_POLYGON

    display()
    pygame.display.flip()
    pygame.time.wait(25)
pygame.quit()
