__author__ = 'rakesh'


x = 'HELLOWORLD'

y = []

for i in range(len(x)):

    k = ord(x[i]) - 5

    if k < 65:

        k = 90 - (65 - k - 1)

    elif k > 90:

        k = 65 + (k - 90 - 1)

    y.append(chr(k))

print "".join(y)
















