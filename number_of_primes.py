__author__ = 'rakesh'


def getPrimeNumbers(N):

    prime_numbers = [2, 3]

    for i in range(4, N):

        p = prime(i)

        if p == 0:
            prime_numbers.append(i)

    print len(prime_numbers)


def prime(i):

    j = 2

    count = 0

    while j < i:

        if i % j != 0:
            j = j + 1

        else:
            count = 1
            break

    return count

getPrimeNumbers(100)















