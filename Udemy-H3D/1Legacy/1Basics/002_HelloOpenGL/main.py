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

    
    glBegin(GL_POINTS) # start drawing

    glVertex2i(50, 200) # draw a point
    glVertex2i(75, 150) # draw a point
    glVertex2i(82, 160) # draw a point
    glVertex2i(100, 210) # draw a point
    glVertex2i(120, 100) # draw a point
    glVertex2i(150, 100) # draw a point
    glVertex2i(180, 105) # draw a point
    glVertex2i(190, 190) # draw a point
    glVertex2i(195, 230) # draw a point
    glVertex2i(230, 290) # draw a point
    glVertex2i(240, 300) # draw a point
    glVertex2i(250, 306) # draw a point
    glVertex2i(280, 290) # draw a point
    glVertex2i(290, 343) # draw a point
    glVertex2i(280, 386) # draw a point

    glEnd() # stop drawing


    # game loop
    for event in pygame.event.get():

        if event.type == QUIT:
            quit_game()





    pygame.time.wait(100)


