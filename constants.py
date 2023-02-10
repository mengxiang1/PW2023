import numpy

#color constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (150, 113, 86)
GREY = (192, 192, 192)
DARK_GREY = (48, 48, 48)
RED = (255, 0, 0)

DIAGONALS = numpy.array([
    [
        [0, 0, 0, 0, 1],
        [0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0]
    ],
    [
        [1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1]
    ]])
HORIZONTAL = numpy.array(
    [
        [1, 1, 1, 1, 1]
    ])
VERTICAL = numpy.array(
    [
        [1],
        [1],
        [1],
        [1],
        [1]
    ])