__author__ = 'rakesh'


# print out the highest palindrome and length of each palindrome exist in the string

def Palindrome(text):

    list = []
    palindrome = []
    new_list = []
    f = []

    for k in range(0, len(text)):
        list.append(text[k])

    j = len(text) - 1
    i = 0
    print i, j

    def LP(i, j):

        if j == 0:
            return 1
        elif i == j:
            return 1
        elif j == (i + 1) and text[i] != text[j]:
            return 1
        elif j == (i + 1) and text[i] == text[j]:
            return 2
        elif text[i] == text[j]:
            palindrome.append(list[i:j+1])
            return LP(i+1, j-1) + 2
        else:
            return max(LP(i+1, j), LP(i, j-1))

    print LP(i, j)

    for i in range(0, len(palindrome)):
        new_list.append("".join(palindrome[i]))


    for line in new_list:
        if Palindrome_print(line) == 1:
            f.append(line)

    for line in set(f):
        print line, len(line)

def Palindrome_print(string):
    x = len(string)
    count = 1

    for i in range(0, x/2):
        if string[i] != string[x-1]:
            count = 0
        x = x -1

    return count

Palindrome("")










