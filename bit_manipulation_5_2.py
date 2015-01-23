__author__ = 'rsukla'
'''
Given a real number between 0 and 1 (e.g., 0.72) that is passed in as a double,
print the binary representation. If the number cannot be represented accurately
in binary with at most 32 characters, print "ERROR
'''

# Firstly , whether we have the concept of double in python ?

# representing a decimal number in binary is more difficult and you can see the reason , write a code to make it easier
# for me

x = input("Input a real number between 0 an 1")  # passed it as float

def realToBinary(x):
    list = []
    global i
    y = x * 2

    while not y == 1.0:
        y = x * 2
        if y == 1:
            break
        if y > 1:
            list.append(1)
            x = y - 1
        else:
            list.append(0)
            x = y

        print y
    list.append(1)
    return list

print (realToBinary(x))

'''
0.72 * 2 = 1
0.44 * 2 = 0
0.88 * 2 = 10.
0.76 * 2 = 1
0.52 * 2 = 1
0.04 * 2 = 0
0.08 * 2 = 0
0.16 * 2 = 0
0.32 * 2 = 0
0.64 * 2 = 1
0.28 * 2 = 0
0.56 * 2 = 1
0.12 * 2 = 0
0.24 * 2 = 0
0.48 * 2 = 0
0.96 * 2 = 1
0.92 * 2
'''