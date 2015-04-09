__author__ = 'rakesh'


array = []

for i in range(0, 100):
    array.append('{0:08b}'.format(i))

def missingElement(A):

    for i in range(len(A)):

        if '{0:08b}'.format(A[i]) in array:
            array.remove('{0:08b}'.format(A[i]))  #everything is happening in O(n) time here

    return array

print missingElement([88, 105, 3, 2, 200, 0, 10])









