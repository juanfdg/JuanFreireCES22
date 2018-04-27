"""Wrong MRO example with crossed inheritance. Should raise an error"""


class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


class E(C, B):
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
