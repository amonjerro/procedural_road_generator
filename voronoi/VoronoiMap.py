import random
import queue

from graph import Vertex
from voronoi.events import SiteEvent


class VoronoiMap:
    def __init__(self, map_x, map_y, seed_amount=10, seeds=None):
        if seeds:
            self.seeds = [Vertex(seed[0], seed[1]) for seed in seeds]
        else:
            self.seeds = [Vertex(random.randint(0,map_x), random.randint(0, map_y)) for i in range(seed_amount)]
        
        self.event_queue = queue.PriorityQueue()
        self.event = None

        self.status_tree = None
        
    def initialize(self):
        for seed in self.seeds:
            site_event = SiteEvent(seed)
            self.event_queue.put(site_event)
        return self.event_queue