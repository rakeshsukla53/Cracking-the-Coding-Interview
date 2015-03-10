__author__ = 'rakesh'

#using heapq library to implement heap sort in python

import heapq

def heapsort(list):
    h = []
    for value in list:
        heapq.heappush(h, value)

    return [heapq.heappop(h) for i in range(len(h))]


print heapsort([5, 6, 7, 10, 123, 100, 11])

#A heapsort can be implemented by pushing all the values into the heap first and then popping out smallest value one by
#one
#one of the best advantage of this is that you can insert tuples as well and do some calculation

'''
>>> h = []
>>> heappush(h, (5, 'write code'))
>>> heappush(h, (7, 'release product'))
>>> heappush(h, (1, 'write spec'))
>>> heappush(h, (3, 'create tests'))
>>> heappop(h)
(1, 'write spec')
'''

