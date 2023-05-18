import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Utils import *
import random as rn
from pre import *

pygame.init()

screen_width = 800
screen_height = 800
ortho_left = -400
ortho_right = 400
ortho_top = -400
ortho_bottom = 400

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
stack = []
rule_run_number = 7
instructions = ""

pre_comp = False


def run_rule(run_count, pre = None):
    global instructions, angle, current_position, comp_pos
    instructions = axiom

    if pre != None:
        angle = pre['angle']
        current_position = (pre['x'], pre['y'])
        comp_pos = current_position
        instructions = pre['data']
        return True

    for loops in range(run_count):
        old_system = instructions
        instructions = ""
        for c in range(0, len(old_system)):
            if old_system[c] in rules:
                instructions += rules[old_system[c]]
            else:
                instructions += old_system[c]
    
    print("Rule")
    print(instructions)
    return False



def save_pat(name: str):
    path = 'Udemy-H3D/1Legacy/1Basics/014_Fractals_turtle/pre.py'
    if pre_comp:
        return 0

    result = {}
    f = open(path, "w")

    result['angle'] = angle
    result['x'] = current_position[0]
    result['y'] = current_position[1]
    result['data'] = instructions
    
    f.write(name + " = " + str(result))


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


def move_to(pos):
    global current_position
    current_position = (pos[0], pos[1])


def reset_turtle():
    global current_position, direction, pre_comp

    if pre_comp:
        current_position = comp_pos
        direction = np.array([0, 1, 0])
        return 0

    current_position = (0, 0)
    direction = np.array([0, 1, 0])


def draw_turtle():
    global direction

    for c in range(0, len(instructions)):
        # glColor(rn.randint(0, 1), rn.randint(0, 1), rn.randint(0, 1), 1)
        
        if instructions[c] in ('F', 'G', 'A', 'B'):
            forward(draw_length)

        elif instructions[c] == '+':
            rotate(angle)
        
        elif instructions[c] == '-':
            rotate(-angle)
        
        elif instructions[c] == '[':
            stack.append((current_position, direction))
        
        elif instructions[c] == ']':
            current_vector = stack.pop()
            move_to(current_vector[0])
            direction = current_vector[1]


def forward(draw_length = 50):
    new_x = current_position[0] + direction[0] * draw_length
    new_y = current_position[1] + direction[1] * draw_length
    line_to(new_x, new_y)


def rotate(angle):
    global direction
    direction = z_rotation(direction, math.radians(angle))





init_ortho()
done = False
glLineWidth(1)

pre_comp = run_rule(rule_run_number)
save_pat('Sierpinski_triangle')
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glBegin(GL_POINTS)
    glVertex2f(0, 0)
    glEnd()


    reset_turtle()
    draw_turtle()

    pygame.display.flip()
pygame.quit()

