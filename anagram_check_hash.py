__author__ = 'rakesh'

#print all combination of a given string for example abc , a,b,c ,ab, bc, ac, abc

import hashlib

x = "rakesh"
y = "arkesh"

dict1 = { }
dict2 = { }

for i in range(0, len(x)):
    dict1[i] = y[i]
    dict2[i] = x[i]

print sorted(dict1.values())

print dict1

p = dict1.__cmp__(dict2)

print p






