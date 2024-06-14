''' Concept of ternary operator '''
# Given
# grade = int(input("Enter student's grade: "))

# INEFFICIENT way of doing this:
# if grade >= 65: # student passes
#     result = "P"
# else:
#     result = "F"
# EFFICIENT way of doing this
# result = "P" if grade >=65 else "F"

# print(result)



''' How can it be used in list comprehension? '''
''' Problem 1 '''
# Given
grades = [84, 99, 55, 65, 64, 78]
# Result: ['P', 'P', 'F', 'P', 'F', 'P']
result = ['P' if grade >= 65 else "F" for grade in grades]
print(result)


''' Problem 2 '''
# Given
grades = [84, 99, 55, None, 65, 64, 78, None, 0] # final grades, curve by giving each grade +5
# Result: [89, 104, 60, 0, 70, 69, 83, 0, 5]
result = [grade + 5 if type(grade) == int else 0 for grade in grades]
print(result)

















