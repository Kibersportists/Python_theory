# snake case - function names, variables def add_two
# camel case - class name, Student, CreditCard, and not credit_card

class Student:
    
    def __init__(self, name: str, age = 18):
        self.name = name
        self.age = age
        self.courses = [] # CS1114, CS1134
    
    def add_course(self, course):
        if (course in self.courses):
            print("Student is already enrolled in " + str(course))
        else:
            self.courses.append(course)
    
    # dunder method, dunder = double underscore, operator overloading
    def __str__(self): # Turns our student object into a string object
        return "Name: " + self.name + "\nAge: " + str(self.age) + "\nCourses: " + str(self.courses)
    
    def __repr__(self): # This is for the console
        return str(self)

# fields and attributes
# behaviour and methods

# students = [["Kenny", 23], ["Bob", 15]]

s1 = Student("Kenny", 23) # object is an instance of a class
print(s1.name, s1.age)
s1.add_course("CS1134")
s1.add_course("CS1134")
print(s1.courses)
s1.add_course("CS1114")
s1.add_course("CS2124")
print(s1.courses)

print(s1)




