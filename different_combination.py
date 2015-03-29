__author__ = 'rakesh'

'''
import itertools  #this can be easily done by using itertools but you need to implement an algorithm for it

k = itertools.permutations('ABCD', 4)

for line in k:
    print "".join(line)
'''
'''
import itertools

k = itertools.combinations('ABCD', 4)

for line in k:
    print "".join(line)
'''

#https://docs.python.org/2/library/itertools.html the documentation is available here


def permutations(head, tail=''):
    if len(head) == 0: print tail
    else:
        for i in range(len(head)):
            permutations(head[0:i] + head[i+1:], tail+head[i])

permutations("abc")





