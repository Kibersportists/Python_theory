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

    def __str__(self): #for printing and converting to str, represent with a/b
        return str(self.numerator) + "/" + str(self.denominator)

    def __repr__(self):
        return str(self)




#TEST CODE
a = Fraction(3, 4)

#a.__mul__(3)
d = a * 3
print(d)

#3.__mul__(a)
e = 3 * a
print(e)










