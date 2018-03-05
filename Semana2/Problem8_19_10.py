import sys

def reverse(str):
    length = len(str)
    rev = ""
    for i in range(length):
        rev = rev + str[length-i-1]

    return rev


def is_palindrome(str):
    return str == reverse(str)


def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED".format(linenum)

    print(msg)
    

test(is_palindrome("abba"))
test(not is_palindrome("abab"))
test(is_palindrome("tenet"))
test(not is_palindrome("banana"))
test(is_palindrome("straw warts"))
test(is_palindrome("a"))
# test(is_palindrome(""))    # Is an empty string a palindrome?
test(is_palindrome(""))
