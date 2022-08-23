import random

from graph import Vertex
from utils import ColorMaker


class VoronoiMap:
    def __init__(self, map_x, map_y, seed_amount=10, seeds=None):
        if seeds:
            if isinstance(seeds[0], Vertex):
                self.seeds = seeds
            else:
                self.seeds = [Vertex(seed[0], seed[1]) for seed in seeds]
        else:
            self.seeds = [Vertex(random.randint(0,map_x-1), random.randint(0, map_y-1)) for i in range(seed_amount)]
        
        self.region_colors = [ColorMaker.make_color_rgb() for seed in self.seeds]
        self._height = map_y
        self._width = map_x
        
        self._edges = list()
        self._vertices = set()
        self._pixels = []
        self.distance = None

    def make_map(self):
        self._pixels = []
        for y in range(self._height):
            self._pixels.append([])
            for x in range(self._width):
                min_distance = float("inf")
                cluster = -1
                for i in range(len(self.seeds)):
                    if self.distance(self.seeds[i], Vertex(x,y)) < min_distance:
                        cluster = i
                
                self._pixels[y].append(self.region_colors[i])

    def set_distance(self, distance_func):
        self.distance = distance_func
    
    def get_seeds(self):
        return self.seeds