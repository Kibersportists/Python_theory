#Complete the following class
'''
Modify __mul__ to support multiplication with int:
ex) a = Fraction(3,4) #3/4
    b = a*3
    print(b) # 9/4


Add __rmul__ to support right hand miliplication with int:
ex) a = Fraction(3,4) #3/4
    b = 3 * a
    print(b) # 9/4

'''

class Fraction:
    def __init__(self, numerator, denominator = 1):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        new_numerator = self.numerator*other.denominator + self.denominator*other.numerator
        new_denominator = self.denominator*other.denominator
        return Fraction(new_numerator, new_denominator)    

    def __sub__(self, other):
        new_numerator = self.numerator*other.denominator - self.denominator*other.numerator
        new_denominator = self.denominator*other.denominator
        return Fraction(new_numerator, new_denominator) 
    
    #cross multiply
    def __mul__(self, other):
        if isinstance(other, int):
            return Fraction(self.numerator * other, self.denominator) # a * 3 = a.__mul__()
        else:
            new_numerator = self.numerator*other.numerator
            new_denominator = self.denominator*other.denominator
        return Fraction(new_numerator, new_denominator)
    
    def __rmul__(self, other):
        return self * other # self.__mul__(other)

    #reciprocate and cross multiply; truediv = /, floordiv = //, mod = %
    def __truediv__(self, other):
        new_numerator = self.numerator*other.denominator
        new_denominator = self.denominator*other.numerator
        return Fraction(new_numerator, new_denominator) 
    
    # Sorting Methods
    def __lt__(self, other):
        numerator1 = self.numerator*other.denominator
        numerator2 = self.denominator*other.numerator
        return numerator1 < numerator2
    
    def __gt__(self, other):
        numerator1 = self.numerator*other.denominator
        numerator2 = self.denominator*other.numerator
        return numerator1 > numerator2
    
    def __eq__(self, other):
        return not (self < other or self > other)
    
    def __ne__(self, other):
        return not (self == other)

    def __le__(self, other):
        return self < other or self == other
    
    def __ge__(self, other):
        return self > other or self == other

    # String method for object
    def __str__(self): #for printing and converting to str, represent with a/b
        return str(self.numerator) + "/" + str(self.denominator)

    def __repr__(self):
        return str(self)




#TEST CODE
Fractions = [Fraction(3, 4), Fraction(2, 5), Fraction(-3, 6), Fraction(6, 8)]
# print(Fractions)
# Fractions.sort()
# print(Fractions)



a = Fraction(2, 4)
b = Fraction(1,3)
c = Fraction(1, 2)

print("a < b", a < b) # False
print("a > b", a > b) # True
print("a == c", a == c) # True





