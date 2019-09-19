## made by Lucka Barbeau 1748294 and Matthew Coffey 1642072
from read_file import read_file
import numpy as np

expectedOutput = np.array([[79.95840, 78.85821, 73.52985, 51.07365],
                           [181.44948, 177.23744, 158.37760, 97.80701]])

functionOutput = read_file("p242_T_directe_4x2.txt")

if np.array_equal(expectedOutput, functionOutput):
    print('Test passed.')

else:
    print('Test failed. Array was not properly created from input file.')


