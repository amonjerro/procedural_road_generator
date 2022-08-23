from utils.distance import euclidean_distance
from utils.distance import manhattan_distance
from utils.colors import ColorMaker


def flatten(arr):
    returnable = []
    for level in arr:
        returnable += level
    return returnable