__author__ = 'rakesh'


#Given an array of integers, every element appears twice except for one. Find that single one.
#Note:
#Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

a = [7, 2, 2, 3, 3, 4, 4, 55, 55, 100, 100]


b = 0

for num in a :    #use XOR to iterate over the do the solution

    print "b = %d" %b
    print "num = %d" %num
    b ^= num
    print "result = %d" %b
    print '\n'

#for i in range(len(a)):


#you will find the forever alone element in the array 






