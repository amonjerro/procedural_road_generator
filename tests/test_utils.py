from graph.vertex import Vertex
from utils import euclidean_distance
from utils import manhattan_distance
from utils import flatten
from utils import ColorMaker

class TestDistances:
    def test_euclidean_distance_two_dimensions(self):
        vertexA = Vertex(0,0)
        vertexB = Vertex(3,4)

        assert euclidean_distance(vertexA, vertexB) == 5
    
    def test_manhattan_distance_two_dimensions(self):
        vertexA = Vertex(0,0)
        vertexB = Vertex(1,2)

        assert manhattan_distance(vertexA, vertexB) == 3
    
    def test_flatten(self):
        # Arrange
        a = [[1,2,3],[4,5,6]]
        
        # Act
        b = flatten(a)

        # Assert
        assert b == [1,2,3,4,5,6]

    def test_color_maker(self):
        color = ColorMaker().make_color_rgb()

        assert len(color) == 3
        assert color[0] > 0 and color[0] < 256
        assert color[1] > 0 and color[1] < 256
        assert color[2] > 0 and color[2] < 256
