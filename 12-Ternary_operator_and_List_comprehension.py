''' Problem 1 '''
# Generate a List containing letter A-Z all uppercase (use chr(i) to convert numbers to ASCII)
# Result: ['A', 'B', 'C', 'D', 'E', ... , 'Z']
result = [chr(i) for i in range(65, 91)]
print(result)


''' Problem 2 '''
# Generate a list containing the following integers
# Result: [1, 2, 4, 8, 16, 32, 64, 128]
result = [2**power for power in range(8)]
print(result)


''' Problem 3 '''
# Generate a list containing the following integers
# Result: [1, 22, 333, 4444, 55555]
# result = [int(chr(index)) for index in range(1, 2)]
result = [int(str(i)*i) for i in range(1, 6)]
print(result)


''' Problem 4 '''
# Given
s = "Watermelon"
# Generate a list containing the characters of s, where all chars at even indices are lower case
# and all chars at odd indices are upper case. Hint: Use the ternary operator.
# Result: ['w', 'A', 't', ... 'N']
result = [s[index].lower() if index%2==0 else s[index].upper() for index in range(len(s))]
print(result)


''' Problem 5 '''
# Given
# s = input("Enter a word")
# Generate a list containing the characters of s (user-input) repeated twice
# DO NOT USE ANY MATH OPERATORS s*2 or ADD s+s!
s = "Python"
# Result: ['P', 'y', .... , 'n', 'P', ... , 'n']
# s = "Java"
# Result: ['J', 'a', 'v', 'a', 'J', 'a', 'v', 'a']
# NOT ALLOWED: result = [[s[index] if index < len(s) else s[index-len(s)] for index in range(0, len(s)*2)]]
result = [s[index] for index in range(-len(s), len(s))]
print(result)



''' PYTHON HAS NEGATIVE INDICES!!!
len("Python") = 6
0   1   2   3   4   5
P   y   t   h   o   n
-6  -5  -4  -2  -1  0
'''









