from roadmap import Vertex

class SiteEvent:
    def __init__(self, vertex:Vertex):
        self.vertex = vertex
    
class CircleEvent:
    def __init__(self, center:Vertex, radius, arc_node, point_triple=None, arc_triple=None):
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