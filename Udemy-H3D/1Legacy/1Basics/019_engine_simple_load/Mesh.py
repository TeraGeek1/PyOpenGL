from OpenGL.GL import *
from pygame.locals import *


class Mesh:
    def __init__(self):
        self.vertices = [
            (0.5, -0.5, 0.5),
            (-0.5, -0.5, 0.5),
            (0.5, 0.5, 0.5),
            (-0.5, 0.5, 0.5),
            (0.5, 0.5, -0.5),
            (-0.5, 0.5, -0.5),
        ]

        self.color = [[1, 1, 1, 1]]
        self.triangles = [0, 2, 3, 0, 3, 1]
        self.draw_type = GL_LINE_LOOP

    def draw(self):
        color_idx = 0
        for t in range(0, len(self.triangles), 3):
            glBegin(self.draw_type)
            glColor(
                self.color[color_idx][0],
                self.color[color_idx][1],
                self.color[color_idx][2],
                1,
            )
            glVertex3fv(self.vertices[self.triangles[t]])
            glVertex3fv(self.vertices[self.triangles[t + 1]])
            glVertex3fv(self.vertices[self.triangles[t + 2]])
            glEnd()
            color_idx += 1
