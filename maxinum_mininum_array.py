__author__ = 'rakesh'

'''
Given an array of integers which is initially increasing and then decreasing, find the maximum value in the array.

Input: arr[] = {8, 10, 20, 80, 100, 200, 400, 500, 3, 2, 1}
Output: 500

Input: arr[] = {1, 3, 50, 10, 9, 7, 6}
Output: 50

Corner case (No decreasing part)
Input: arr[] = {10, 20, 30, 40, 50}
Output: 50

Corner case (No increasing part)
Input: arr[] = {120, 100, 80, 20, 0}
Output: 120
'''
'''
Idea - The maxinum element will be greater than next and previous element
Use divide and conquer example
we will also use the recursive approach here
'''


def maxinum(A):

    i = 0
    j = len(A) - 1
    mid = (j + i) / 2
    if mid == 0:
        print A[mid+1]
    if A[mid] > A[mid-1] and A[mid] < A[mid+1]:
        maxinum(A[mid:])
    elif A[mid] < A[mid-1] and A[mid] > A[mid+1]:
        maxinum(A[:mid])

    elif A[mid] > A[mid + 1] and A[mid] > A[mid - 1]:
        print A[mid]
        exit(0)


maxinum([10, 20,30, 40, 50, 60, 100, 80, 70])







