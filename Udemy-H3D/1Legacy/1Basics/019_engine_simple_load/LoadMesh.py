from OpenGL.GL import *
from pygame.locals import *
from Mesh import *
from random import randint  # , uniform # Random float in range


class LoadMesh(Mesh):
    def __init__(self, filename, draw_type):
        self.vertices = []
        self.triangles = []
        self.color = []
        self.filename = filename
        self.draw_type = draw_type
        self.load_drawing()

    def load_drawing(self):
        with open(self.filename) as fp:
            line = fp.readline()

            while line:
                color = [0, 0, 0]
                while (color[0] + color[1] + color[2] <= 0) or (
                    color[0] + color[1] + color[2] == 3
                ):
                    color = [randint(0, 1), randint(0, 1), randint(0, 1), 1]
                self.color.append(color)

                if line[:2] == "v ":
                    vx, vy, vz = [float(value) for value in line[2:].split()]
                    self.vertices.append((vx, vy, vz))

                if line[:2] == "f ":
                    t1, t2, t3 = [value for value in line[2:].split()]
                    self.triangles.append(
                        [int(value) for value in t1.split("/")][0] - 1
                    )
                    self.triangles.append(
                        [int(value) for value in t2.split("/")][0] - 1
                    )
                    self.triangles.append(
                        [int(value) for value in t3.split("/")][0] - 1
                    )

                line = fp.readline()
