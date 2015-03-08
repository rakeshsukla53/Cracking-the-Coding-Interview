__author__ = 'rakesh'


#print all combination of 3 tuples using in the list

x = 'ABCD'

length = len(x)

count = 0

for i in range(0, length):
    for j in range(0, length):
        for k in range(0, length):
            for l in range(0, length):
                if i == j == k == l:
                    continue
                else:
                    y = (x[i], x[j], x[k], x[l])
                    if len(set(y)) == 4:
                        print "".join(y)


#the complexity if extremely high for this 






