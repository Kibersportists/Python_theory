''' PROBLEM 1'''
# Given
s = "Watermelon"
# Result: ['W', 'A', 'T', 'E', 'R', 'M', 'E', 'L', 'O', 'N']
result = [char.upper() for char in s]
print(result)


''' PROBLEM 2'''
# Given
s = "Watermelon"
# Result: ['W', 't', 'r', 'm', 'l', 'n']
result = [char for char in s if char not in 'aoeiAOEI']


''' PROBLEM 3'''
# Given
s = "Watermelon"
# Result: ['W', 'a', 't', 'e', 'r']
result = [s[index] for index in range(5)]
print(result)


''' PROBLEM 4'''
# Given
s = "Watermelon"
# Result: ['n', 'o', 'l', 'e', 'm', 'r', 'e', 't', 'a', 'W']
result = [s[index] for index in range(len(s)-1, -1, -1)]
print(result)





