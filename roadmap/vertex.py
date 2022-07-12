import numpy as np

class Vertex:
    def __init__(self, x, y):
        self.coordinates = np.array([x,y])
        self.x = x
        self.y = y
        self.neighbors = []
    