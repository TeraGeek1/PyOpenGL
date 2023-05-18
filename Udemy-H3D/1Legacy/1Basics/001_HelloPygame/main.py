import pygame
import sys
from pygame.locals import *


# lib inits
pygame.init()


# init screen
screen_width = 1600
screen_hight = screen_width / 2
screen = pygame.display.set_mode((screen_width, screen_hight), DOUBLEBUF | OPENGL)
pygame.display.set_caption('OpenGL in Python')


# inti clock
clock = pygame.time.Clock()


def quit_game():
    pygame.quit()
    sys.exit()


while True:

    # display
    pygame.display.flip()
    

    # event loop
    for event in pygame.event.get():

        if event.type == QUIT:
            quit_game()

    


    pygame.time.wait(100)