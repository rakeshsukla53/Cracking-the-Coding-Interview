__author__ = 'rakesh'

import math
'''
Q3. Write a code to find all subsets of a given set:-
Exp: {1,2,3} will give {1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}

'''

'''
Input: Set[], set_size
1. Get the size of power set
    powet_set_size = pow(2, set_size)
2  Loop for counter from 0 to pow_set_size
     (a) Loop for i = 0 to set_size
          (i) If ith bit in counter is set
               Print ith element from set for this subset
     (b) Print seperator for subsets i.e., newline
'''
'''
Example:

Set  = [a,b,c]
power_set_size = pow(2, 3) = 8
Run for binary counter = 000 to 111

Value of Counter            Subset
    000                    -> Empty set
    001                    -> a
    011                    -> ab
   100                     -> c
   101                     -> ac
   110                     -> bc
   111                     -> abc
'''

def subsets():

    t = [1, 2, 3]

    subset = []

    l = len(t)

    power_set = int(math.pow(2, l))

    for i in range(0, power_set):

        x = str('{0:03b}'.format(i))

        subset = []

        for j in range(0, len(x)):

            if x[j] == '1':

                subset.append(str(t[j]))

        print "".join(subset)

    #'{0:03b}'.format(7)  # this is convert into binary  03 decides the number of bits of the binary number


subsets()







#if you want to understand the {0 : 08b}.format(8)



'''
Just to explain the parts of the formatting string:

    {} places a variable into a string
    0 takes the variable at argument position 0
    : adds formatting options for this variable (otherwise it would represent decimal 6)
    08 formats the number to eight digits zero-padded on the left
    b converts the number to its binary representation
'''









