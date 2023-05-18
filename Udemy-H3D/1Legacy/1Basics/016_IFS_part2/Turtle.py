import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Utils import *
from random import randint

pygame.init()

screen_width = 800
screen_height = 800
ortho_left = 0
ortho_right = 800
ortho_top = 0
ortho_bottom = 800

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Turtle Graphics')


current_position = (0, 0)
direction = np.array([0, 1, 0])

axiom = 'F-G-G'
rules = {
    'F': 'F-G+F+G-F',
    'G': 'GG',
    'A': 'B-A-B',
    'B': 'A+B+A'
}
draw_length = 5
angle = 120

points = []
x, y = 0, 0



def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(ortho_left, ortho_right, ortho_top, ortho_bottom)


def line_to(x: GL_FLOAT, y: GL_FLOAT):
    global current_position

    glBegin(GL_LINE_STRIP)
    glVertex2f(current_position[0], current_position[1])
    glVertex2f(x, y)
    current_position = (x, y)
    glEnd()


def draw_points():
    glBegin(GL_POINTS)
    for p in points:
        glColor(p[2], p[3], p[4], 1)
        glVertex2f(p[0], p[1])
    glEnd()


def move_to(pos):
    global current_position
    current_position = (pos[0], pos[1])


def reset_turtle():
    global current_position, direction

    current_position = (0, 0)
    direction = np.array([0, 1, 0])


def draw_turtle():
    global points, x, y

    points.append((x, y, randint(0, 1), randint(0, 1), randint(0, 1)))
    r = np.random.rand()
    if r < 0.33:
        x, y = 0.5 * x + 0.00 * y + 0.0, 0.00 * x + 0.5 * y + 0.5

    elif r < 0.66:
        x, y = 0.5 * x + 0.00 * y + 0.5, 0.00 * x + 0.5 * y + 0.0

    else:
        x, y = 0.5 * x + 0.00 * y + 0.0, 0.00 * x + 0.5 * y + 0.0

def forward(draw_length = 50):
    new_x = current_position[0] + direction[0] * draw_length
    new_y = current_position[1] + direction[1] * draw_length
    line_to(new_x, new_y)


def rotate(angle):
    global direction
    direction = z_rotation(direction, math.radians(angle))





init_ortho()
done = False
glPointSize(1)
glColor3f(0, 1, 0)


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glScaled(800, 800, 1)

    reset_turtle()
    draw_turtle()
    draw_points()

    pygame.display.flip()
    # pygame.time.wait(100)
pygame.quit()

