## made by Lucka Barbeau 1748294 and Matthew Coffey 1642072
import numpy as np


def read_file(filename):
    file = open(filename, "r")
    i = 1
    j = 0
    k = 0
    for x in file:
        if i == 1:
            nb_x = int(x)
        if i == 2:
            nb_y = int(x)

        if i == 3:
            A = np.zeros((nb_x, nb_y))
            A[j, k] = float(x)
            if j < nb_x:
                j = j + 1
            else:
                j = 0
                k = k + 1
        if i > 3:
            A[j, k] = x
            if (j + 1) < nb_x:
                j = j + 1
            else:
                j = 0
                k = k + 1
        i = i + 1

    A = A.transpose()

    return A
