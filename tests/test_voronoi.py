from graph.vertex import Vertex
from voronoi import VoronoiMap
from utils import euclidean_distance
from utils import manhattan_distance

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
    
    def test_distance_calc(self):
        #Arrange
        vertex_seeds = [Vertex(0,0), Vertex(3,4), Vertex(6,8)]
        vmap = VoronoiMap(10, 10, seeds=vertex_seeds)
        vmap.set_distance(euclidean_distance)

        #Act
        seeds = vmap.get_seeds()
        distance = vmap.distance(seeds[0], seeds[1])

        #Assert
        assert distance == 5
    
    def test_make_map(self):
        map_height = 10
        map_width = 10
        vertex_seeds = [Vertex(1,3), Vertex(4,4), Vertex(6,8)]
        vmap = VoronoiMap(map_width, map_height, seeds=vertex_seeds)

        vmap.set_distance(euclidean_distance)
        vmap.make_map()

        non_tuples = [len(list(filter(lambda x: not isinstance(x, tuple), i))) for i in vmap._pixels]
        non_conforming_pixels = list(filter(lambda x: x > 0, non_tuples))

        assert len(vmap._pixels) == map_height
        assert len(vmap._pixels[0]) == map_width
        assert len(non_conforming_pixels) == 0
    
    def test_color_variety(self):
        vertex_seeds = [Vertex(1,3), Vertex(4,4), Vertex(6,8)]
        vmap = VoronoiMap(10, 10, seeds=vertex_seeds)
        
        colors = vmap.get_colors()

        assert len(colors) == len(vertex_seeds)