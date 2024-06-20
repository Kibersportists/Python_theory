'''
algorithm = solution to a problem
(asymtotic) runtime = total number of operations performed based on input size
asymptotic - (of a function) approaching a given value as an expression containing a variable tends to infinity

runtime reffered to as
big O =  upper bound (worst case)
big Θ (theta) average case = tight bound (between worst and best case)
big Ω = lower bound (best case) - we don't care about this one

For integers and floats, each of the following PRIMITIVE OPERATIONS is 1 operation cost:
assignment operation: =
arithmetic operations: + - * / % //
comparison operations: < > <= >= == !=

print(), you can treat as 1 operation since it is mainly used for debugging,
but it also depends on what you're printing, in this case,
if you are printing an integer, or any of those operations, treat it as 1 operation

If an operation costs of a line is 2, 3, etc (any constant number), treat it as 1 constant operation O(1)
so if you had 1 + 1 + 2 + 1, that would be O(1) in total, each number is constant

constant = O(1)     ex) 1, 10, 500, 200000, etc = O(1)
linear = O(n)       ex) n, 2n, 5n, 3n + 4, n + 5, etc O(n)
quadratic = O(n^2)  ex) n^2, 10n^2, 10n^2 + 2n, etc = O(n^2)
'''

# Write a function that tahes in n, an integer, and returns the number of factors that n has
# ex) 12 has factors [1, 2, 3, 4, 6, 12] --> so there are 6 factors
# ex) 21 has factors [1, 3, 7, 21] --> so there are 4 factors
# ex) 100 has factors [1, 2, 4, 5, 10, 20, 25, 50, 100] --> so there are 9 factors
# Analyze the runtime of your function


# Simplest solution
# def num_of_factors(n: int) -> int: # Linear solution -> O(n)
#     factor_count = 0 # O(1)
#     for i in range(1, n + 1): # O(n)
#         if n % i == 0: # O(1)
#             factor_count += 1 # O(1)
#     return factor_count

import math
def num_of_factors(n: int) -> int: # Linear solution -> 4 + 2*sqrt(n) -> O(n)
    sqrt_of_n = n**0.5 # O(1)
    factor_count = 1 if sqrt_of_n.is_integer() else 0 # O(1)
    sqrt_of_n = math.ceil(sqrt_of_n) # O(1)
    i = 1 # O(1)
    for i in range(1, sqrt_of_n): # sqrt(n) = O(n)
        if n % i == 0: # O(1)
            factor_count += 2 # O(1)
    return factor_count

print("Factor count: ", num_of_factors(12))
print("Factor count: ", num_of_factors(21))
print("Factor count: ", num_of_factors(100))












