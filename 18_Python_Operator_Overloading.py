#Complete the following class
'''
Complete the Fraction class to represent fraction numbers, as oppose to floats.
When printed, the format should be a/b, a being the numerator and b being the denominator.

*YOU DO NOT NEED TO SIMPLIFY THE FRACTIONS* ex) 2/4 doesn't need to be simplified to 1/2
*ASSUME THE NUMERATOR OR DENOMINATOR IS NEVER 0.*

The Fraction class has two data members: numerator and denominator.
__add__ takes in another fraction and returns a new Fraction object with the sum of the 2 fractions
__sub__ takes in another fraction and returns a new Fraction object with the difference of the 2 fractions
__mul__ takes in another fraction and returns a new Fraction object with the product of the 2 fractions 
__truediv__ takes in another fraction and returns a new Fraction object with the quotient of the 2 fractions 
'''

class Fraction:
    def __init__(self, numerator, denominator = 1):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
    

    def __sub__(self, other):
    
    
    #cross multiply
    def __mul__(self, other):


    #reciprocate and cross multiply; truediv = /, floordiv = //, mod = %
    def __truediv__(self, other):


    def __str__(self): #for printing and converting to str, represent with a/b


    def __repr__(self):
        return str(self)




#TEST CODE
a = Fraction(3, 4)
b = Fraction(2, 7)
c = Fraction(5)

# print(a)    #3/4
# print(b)    #2/7
# print(c)    #5/1


# print("\nTesting Add:")
# print("a+b =", a + b)   #a+b = 29/28
# print("b+a =", b + a)   #b+a = 29/28 


# print("\nTesting Subtract;")
# print("a-b =", a - b)   #a-b = 13/28
# print("b-a =", b - a)   #b-a = -13/28


# print("\nTesting Multiply:")
# print("a*b =", a * b)   #a*b = 6/28
# print("b*a =", b * a)   #b*a = 6/28


# print("\nTesting Divide:")
# print("a/b =", a / b)   #a/b = 21/8
# print("b/a =", b / a)   #b/a = 8/21









