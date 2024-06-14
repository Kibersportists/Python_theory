# dunder methods
# dunder = double underscore

# Operators +, -, *, /, ==, +=, -=, etc.

#Complete the following class
'''
Complex Numbers: https://www.mathsisfun.com/numbers/complex-numbers.html

Operator Overloading

i = sqrt(-1), i^2 = -1
Create a Complex class representing the format a + bi, a = constant, b = coefficient of i
__add__  -> complex1 + complex2 returns a new Complex object with the sum of 2 complex nums
__sub__  -> complex1 - complex2 returns a new Complex object with the difference of 2 complex nums
__mul__  -> complex1 * complex2 returns a new Complex object with the product of 2 complex nums

for __mul__, use the FOIL method
a1, a2, b1, b2 are constants, i = imaginary number, i*i = i^2 = -1
ex) (a1 + b1i)(a2 + b2i) = a1*a2 + (a1*b2i) + (a2*b1i) + (b1i*b2i) 
a1*a2 + (a1*b2i) + (a2*b1i) - b1*b2

new a = a1*a2 - b1*b2
new b = a1*b2 + a2*b1

ex) (5 + 2i)(3 + 3i)
'''

class Complex:
    # a + bi
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)
    
    def __sub__(self, other):
        return Complex(self.a - other.a, self.b - other.b)
    
    def __mul__(self, other):
        return Complex((self.a*other.a) - (self.b*other.b), (self.a*other.b) + (self.b*other.a))

    def __str__(self):
        if self.b > 0:
            return str(self.a) + "+" + str(self.b) + "i"
        else:
            return str(self.a) + "" + str(self.b) + "i"



#TEST CODE
'''
def __add__(self, other): 
cplx1 + cplx2
In this example, self refers to cplx1 since it is the first argument 
and other would refer cplx2 since it is the second argument.
'''
# constructor, output
cplx1 = Complex(5, 2)
print(cplx1) 	#5 + 2i
cplx2 = Complex(3, 3)
print(cplx2)	#3 + 3i

# addition
print(cplx1 + cplx2)	#8 + 5i

# subtraction
print(cplx1 - cplx2)	#2 - 1i
print(cplx2 - cplx1)	#-2 + 1i

# multiplication
print(cplx1 * cplx2)	#9 + 21i

# original objects remain unchanged
print(cplx1) 	#5 + 2i
print(cplx2)	#3 + 3i

cplx1 += cplx2
print(cplx1)    #8 + 5i











