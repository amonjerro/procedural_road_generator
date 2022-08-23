from graph import Vertex

class Event:
    circle_event = False

    @property
    def x_coord(self):
        return 0

    @property
    def y_coord(self):
        return 0

    def __lt__(self, other):
        if self.x_coord == other.x_coord and self.y_coord == other.y_coord:
            return self.circle_event and not other.circle_event
        
        if self.y_coord == other.y_coord:
            return self.x_coord < other.x_coord
        
        return self.y_coord > other.y_coord

    def __eq__(self, other):
        if other is None:
            return None
        return self.y_coord == other.y_coord and self.x_coord == other.x_coord
    
    def __ne__(self, other):
        return not self.__eq__(other)


class SiteEvent(Event):
    circle_event = False

    def __init__(self, vertex:Vertex):
        super().__init__()
        self.vertex = vertex
        self.x_coord = vertex.x
        self.y_coord = vertex.y

    def get_x(self):
        return self.x_coord

    def get_y(self):
        return self.y_coord

class CircleEvent(Event):
    circle_event = True

    def __init__(self, center:Vertex, radius, arc_node, point_triple=None, arc_triple=None):
        super().__init__()
        self.isValid = True
        self.center = center
        self.radius = radius
        self.arcNode = arc_node
        self.pointTriple = point_triple
        self.arcTriple = arc_triple
    
    def get_triangle(self):
        return (
            (self.pointTriple[0].x, self.pointTriple[0].y),
            (self.pointTriple[1].x, self.pointTriple[1].y),
            (self.pointTriple[2].x, self.pointTriple[2].y),
        )