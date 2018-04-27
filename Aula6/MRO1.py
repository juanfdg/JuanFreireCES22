"""Normal MRO example with multiple inheritance"""


class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


class E(B, C):
    pass


class F(D, E):
    pass


print(A.mro())
print(B.mro())
print(C.mro())
print(D.mro())
print(E.mro())
print(F.mro())
