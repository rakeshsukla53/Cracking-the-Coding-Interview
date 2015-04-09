__author__ = 'rakesh'


'''
the idea is to create a recursion tree of the string and it will print out all the different combination
'''
'''
A[current], A[start] = A[start], A[current] this type of item assignment is not supported for string.
All int values can be swapped like this
'''
'''
python does not support string assignment either so you need to first convert into a list and then perform all
operation
'''

stringList = []

def permutationString(A, start, end):

    A = list(A)

    if start == end - 1:
       stringList.append("".join(A))  #this is the most important step since it will tell how many

    for current in range(start, end):  #the loop will be determined by the loop and the value of the current
        temp = A[current]
        A[current] = A[start]
        A[start] = temp
        permutationString("".join(A), start + 1, end)

        '''
        temp = A[current]
        A[current] = A[start]
        A[start] = temp
        '''


if __name__ == '__main__':

    string = '123'
    start = 0
    end = len(string)
    permutationString(string, start, end)
    print stringList
