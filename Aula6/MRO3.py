"""Another MRO example with crossed inheritance."""


class A:
    pass


class B:
    pass


class C:
    pass


class D(A, B, C):
    pass


class E(B, A, C):
    pass


try:
    class F(D, E):
        pass
except TypeError:
    print("Cannot create a consistent method resolution")


print(A.mro())
print(B.mro())
print(C.mro())
print(D.mro())
print(E.mro())
