from graph.vertex import Vertex
from voronoi import VoronoiMap

class TestVoronoiMap:
    def test_create_random_seeds(self):
        #Arrange
        seeds_to_create = 3
        vmap = VoronoiMap(10, 10, seeds_to_create)

        #Act
        seeds = vmap.get_seeds()

        #Assert
        assert seeds_to_create == len(seeds)
        for seed in seeds:
            assert isinstance(seed, Vertex)
    
    def test_create_defined_vertex_seeds(self):
        #Arrange
        vertex_seeds = [Vertex(1,3), Vertex(4,4), Vertex(6,8)]
        vmap = VoronoiMap(10, 10, seeds=vertex_seeds)

        #Act
        seeds = vmap.get_seeds()

        #Assert
        assert len(vertex_seeds) == len(seeds)
        for i in range(len(vertex_seeds)):
            assert seeds[i] == vertex_seeds[i]

    def test_create_defined_tuple_seeds(self):
        coordinate_seeds = [(1,3), (4,4), (6,8)]
        vmap = VoronoiMap(10, 10, seeds=coordinate_seeds)

        #Act
        seeds = vmap.get_seeds()

        #Assert
        assert len(coordinate_seeds) == len(seeds)
        for i in range(len(coordinate_seeds)):
            v = Vertex(coordinate_seeds[i][0], coordinate_seeds[i][1])
            assert seeds[i] == v