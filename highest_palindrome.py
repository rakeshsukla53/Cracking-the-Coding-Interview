__author__ = 'rakesh'

#For example, if the given string is forgeeksskeegfor, the output should be geeksskeeg.

#https://www.youtube.com/watch?v=Mbav2iuJ7xQ do refer this video

#LP is longest palindrome sequence

#this program will tell you the highest length of plaindrome we can form using the letters of the string

#For example in the sequence XAYBZBA, longest palindromic subsequence is ABZBA which is of length 5

def Palindrome(text):

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
            return LP(i+1, j-1) + 2
        else:
            return max(LP(i+1, j), LP(i, j-1))

    print LP(i, j)

Palindrome("")










