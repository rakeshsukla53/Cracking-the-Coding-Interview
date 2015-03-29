__author__ = 'rakesh'

#Find the AP difference

N = raw_input("How many values")

value = raw_input("Enter the values")

x = value.split(" ")

print x

d = int(x[1]) - int(x[0])

for i in range(0, len(x) - 1):

     if (int(x[i + 1]) - int(x[i])) != d:

         print int(x[i]) + d









