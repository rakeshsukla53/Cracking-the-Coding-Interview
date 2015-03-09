__author__ = 'rakesh'

#generate randon number in range 1-7 from a function which generates raandom number in range 1-5

import random

def random_one_five():

    x = random.randrange(1, 6, 1)

    return x

def random_one_seven():
    x = random_one_five()
    if x == 4 or x == 5:
        x = random.randrange(4, 8, 1)
        return x
    return x

print random_one_seven()

