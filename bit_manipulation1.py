__author__ = 'rsukla'

'''
You are given two 32-bit numbers, N and M, and two bit positions, land j. Write
a method to insert M into N such that M starts at bit j and ends at bit i. You can
assume that the bits j through i have enough space to fit all of M. That is, if
M = 10011, you can assume that there are at least 5 bits between j and i. You
would not, for example, have j = 3 and i = 2, because M could not fully fit
between bit 3 and bit 2.
EXAMPLE
Input:  N = 10000000000, M = 10011, i = 2, j = 6
Output: N = 10001001100

# Number of bits in M < i - j + 1 if not raise error
# M cannot be greater than n , if it is then you need to raise error

100100
543210  -- Numbering of the bits
'''
'''
N, M = input("Enter two 32 bit number")  If you want to take inputs from the user
J, I = input("Enter the values of I and J")

print(" N = %s M = %s") %(N, M)

print(" J = %s I = %s") %(J, I)
'''

N = 10000000000   #int and str object are immutable ..agar convert karna hain toh split
M = 11111111111
i = 0
j = 10
list = []
#print N, M, i, j

s = 0  #int object ke pass iteration ka option nahi hota you better take care of it

print ("Length of M = %s") %(len(str(M)))
print ("Length of N = %s") %(len(str(N)))

for k in range(0, len(str(N))):
    list.append(str(N)[k])

for k in range((len(str(N))-j) - 1, (len(str(N))-i)):
    if s < len(str(M)):
        list[k] = str(M)[s]
        s = s + 1
    else:
        break
    #list[k] = l
     # Numbering o the index will always be from left to right
      # We can subtract the 11- 6 to get 5 and len(N) - 2 to get number from left to right

print ''.join(list)  #Converting list back to string

'''
for k in range(j, i-1, -1):  # k = 6 , 5, 4, 3, 2
    if s == 0:
        break
    else:
        str(N).split(',')   # int object does not have get item function and str object doesn't support assignment
                                  #Operator
        s = s -1

print N
'''







