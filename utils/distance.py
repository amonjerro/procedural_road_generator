import math

def euclidean_distance(vertexA, vertexB):
    dims = len(vertexA.coordinates)
    return math.sqrt(sum([(vertexA.coordinates[dim]-vertexB.coordinates[dim])**2 for dim in range(dims)]))

def manhattan_distance(vertexA, vertexB):
    dims = len(vertexA.coordinates)
    return sum([abs(vertexA.coordinates[dim]-vertexB.coordinates[dim]) for dim in range(dims)])