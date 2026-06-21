class A:
    label = "A: base class"

class B(A):
    label = "B: Masala blend"

class C(A):
    label = "C: Herbal blend"

class D(C,B): #mro
# class D(B,C): #mro
    pass

cup = D()
#jo bhi phle inherit uska label
print(cup.label)
print(D.__mro__)

# (<class '__main__.D'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)