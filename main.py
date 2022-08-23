from voronoi import VoronoiMap
from imager import create_image
from utils import euclidean_distance, manhattan_distance

if __name__ == '__main__':
    vm = VoronoiMap(680, 680, 12)
    vm.set_distance(manhattan_distance)
    vm.make_map()

    create_image('outputs/test.jpg', vm._pixels)