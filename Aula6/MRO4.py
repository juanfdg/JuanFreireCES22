"""Another MRO example with multiple inheritance.
Result maybe strange for those who don't know how python's C3 linearization algorithm works:
https://medium.com/technology-nineleaps/python-method-resolution-order-4fd41d2fcc"""


class A:
    pass


class B:
    pass


class C:
    pass


class D(A, B):
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
