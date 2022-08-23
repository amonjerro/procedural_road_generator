from graph.vertex import Vertex
from utils import euclidean_distance
from utils import manhattan_distance

class TestDistances:
    def test_euclidean_distance_two_dimensions(self):
        vertexA = Vertex(0,0)
        vertexB = Vertex(3,4)

        assert euclidean_distance(vertexA, vertexB) == 5
    
    def test_manhattan_distance_two_dimensions(self):
        vertexA = Vertex(0,0)
        vertexB = Vertex(1,2)

        assert manhattan_distance(vertexA, vertexB) == 3