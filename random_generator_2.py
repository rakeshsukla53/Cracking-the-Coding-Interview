__author__ = 'rakesh'

#generate randon number in range 1-7 from a function which generates raandom number in range 1-5

import numpy as np
import random


def one_to_five():

    two_D_array = np.array([[1, 2, 3, 4, 5], [6, 7, 1, 2, 3], [4, 5, 6, 7, 1], [2, 3, 4, 5, 6], [7, 0, 0, 0, 0]], int)

    x = random.randrange(1, 6, 1)
    y = random.randrange(1, 6, 1)

    return two_D_array[x-1][y-1]


print one_to_five()




