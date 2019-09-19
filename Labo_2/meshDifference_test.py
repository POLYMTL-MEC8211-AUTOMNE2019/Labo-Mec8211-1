## made by Lucka Barbeau 1748294 and Matthew Coffey 1642072
from meshDifference import meshDifference
import numpy as np


a = np.ones((8, 4))
b = np.zeros((4, 2))
expectedOutput = 32

functionOutput = meshDifference(b, a)

if functionOutput == expectedOutput:
    print('Test passed.')

else:
    print('Test failed. Error between coarse and fine mesh was not calculated properly.')
