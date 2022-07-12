import random

from roadmap import Vertex

class VoronoiMap:
    def __init__(self, map_x, map_y, seed_amount=10, seeds=None):
        if seeds:
            self.seeds = [Vertex(seed[0], seed[1]) for seed in seeds]
        else:
            self.seeds = [Vertex(random.randint(0,map_x), random.randint(0, map_y)) for i in range(seed_amount)]
        self.edges=[]

        self.seeds.sort(key=(lambda x: (x.y, x.x)))

    def fortunes_algorithhm(self):
        site_events = [v for v in self.seeds]
        while len(site_events) > 0:
            p = site_events.pop(0)

    
    def get_vertices(self):
        return [(v.x, v.y) for v in self.seeds]