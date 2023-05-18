import pygame, sys
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def quit_game():
    pygame.quit()
    sys.exit()


# lib inits
pygame.init()


# screen init
screen_width = 1600
screen_hight = screen_width / 2
screen = pygame.display.set_mode((screen_width, screen_hight), DOUBLEBUF | OPENGL)


# Clocks
clock = pygame.time.Clock()


#################### Graphics ####################


def init_ortho():
    '''Init an ortho graphic screen'''
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity() # Clear the GL_PROJECTION
    gluOrtho2D(0, 640, 0, 480) # Setting the coordinate system gluOrtho2D(left:0, Right:640, bottom:0, top:480)



def draw_star(x: int, y: int, size: int):
    glPointSize(size)
    glBegin(GL_POINTS)
    glVertex2d(x, y)
    glEnd()


#################### Graphics ####################


init_ortho()

while True:

    # screen
    pygame.display.flip()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    ##### Draw #####

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity() # Clear the MODEVEIW glLoadIdentity clears what is set in glMatrixMade()
    glPointSize(5)

    draw_star(50, 200, 5) # draw a point
    draw_star(75, 150, 5) # draw a point
    draw_star(82, 160, 7) # draw a point
    draw_star(100, 210, 10) # draw a point
    draw_star(120, 100, 15) # draw a point
    draw_star(150, 100, 5) # draw a point
    draw_star(180, 105, 5) # draw a point
    draw_star(190, 190, 5) # draw a point
    draw_star(195, 230, 10) # draw a point
    draw_star(230, 290, 5) # draw a point
    draw_star(240, 300, 20) # draw a point
    draw_star(250, 306, 5) # draw a point
    draw_star(280, 290, 7) # draw a point
    draw_star(290, 343, 8) # draw a point
    draw_star(280, 386, 6) # draw a point



    # game loop
    for event in pygame.event.get():

        if event.type == QUIT:
            quit_game()





    pygame.time.wait(100)


