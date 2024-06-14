''' PROBLEM 1'''
# Result: [1, 2, 3, 4, 5, 6]
result = [x for x in range(1,7)]
print(result)


''' PROBLEM 2'''
# Result: [1, 4, 9, 16, 25, 36]
result = [x*x for x in range(1,7)]
print(result)


''' PROBLEM 3'''
# Given
lst = [-1, 10, -5, -2, 3, -4]

# Result: [1, 10, 5, 2, 3, 4]
result = [abs(x) for x in lst]
print(result)


''' PROBLEM 4'''
# Given
lst = [-1, 10, -5, -2, 3, -4]

# Result: [-1, -5, -2, -4]
result = [elem for elem in lst if elem < 0]
print(result)


''' PROBLEM 5'''
# Given
lst = [-1, 10, -5, -2, 3, -4]

# Result: 13
result = 0
result = sum([elem for elem in lst if elem > 0])
print(result)


''' PROBLEM 6'''
# Given
lst = [1, 4, 5, 8, 10]

# Result: [2, 3, 6, 7, 9]
result = [x for x in range(1,11) if x not in lst]
print(result)


