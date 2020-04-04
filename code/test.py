import argparse
from array import *

LED_MATRIX_HEIGHT = 13
LED_MATRIX_WIDTH = 23
LED_COUNT = LED_MATRIX_HEIGHT * LED_MATRIX_WIDTH  # Number of LED pixels.


def performToMatrix():
    matrix = [[0 for x in range(LED_MATRIX_HEIGHT)] for y in range(LED_MATRIX_WIDTH)]
    loopIndex = 0

    for x in range(LED_MATRIX_WIDTH):
        for y in range(LED_MATRIX_HEIGHT):
            matrix[x][y] = loopIndex
            loopIndex += 1

    #         before reverse
    for i in matrix:
        print(i)
    print('\n')

    for i in range(LED_MATRIX_HEIGHT):
        if i % 2 == 1:
            matrix[i].reverse()
    return matrix


# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    # matrix = performToMatrix()
    # for i in matrix:
    #     print(i)
    # print(matrix[2][1])
    EOM = "endmsg"
    data = "0 1 2 3 4 5 6 7 8 9 10 11 12 25 38 51endmsg"
    print data
    print(data.strip(EOM).split())
    print list(map(int, data.strip(EOM).split()))
