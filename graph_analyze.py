__author__ = 'rakesh'

'''
graph = {}

graph['1'] = []  #dictionary is obviously mutable

graph['1'].append('x')   #okay so now we can use this functionality to create for graph like structure

print graph
'''


def graph(A):

    path = {}

    for i in range(len(A)):

        if not path.get(A[i][0]):

            path[A[i][0]] = []
            path[A[i][0]].append(A[i][1])

        else:
            path[A[i][0]].append(A[i][1])

    print path

graph([('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'C'), ('E', 'F'), ('F', 'C')])


