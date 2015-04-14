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

    return path

def pathAll(tree, source, destination, path_all = []):  #solved using recursion

    path_all = path_all + list(source)

    if tree.get(source) == None:

        return

    else:
        c = tree.get(source)

        for i in range(len(c)):

            if destination == c[i]:

                path_all.append(destination)
                print path_all
                return

            else:
                pathAll(tree, c[i], destination, path_all)

tree = graph([('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'C'), ('E', 'F'), ('F', 'C')])

pathAll(tree, 'E', 'C')

'''
Output of my graph and how it is connected here. This program is only work for weighted graph and how it can be
{'A': ['B', 'C'],
 'C': ['D'],
 'B': ['C', 'D'],
 'E': ['F'],
 'D': ['C'],
 'F': ['C']}
'''

'''
if tree.get(source) == None:

        return

    else:
        if destination in tree.get(source):
            path_all.append([source, destination])

        else:
            for i in range(len(tree.get(source))):
                path_all(tree, tree.get(source)[i], destination)

'''
