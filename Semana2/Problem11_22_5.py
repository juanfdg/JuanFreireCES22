import sys


def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED".format(linenum)

    print(msg)


def add_vectors(u, v):
    add = []
    if len(u) == len(v):
        for i in range(len(u)):
            add.append(u[i] + v[i])

        return add


test(add_vectors([1, 1], [1, 1]) == [2, 2])
test(add_vectors([1, 2], [1, 4]) == [2, 6])
test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])


