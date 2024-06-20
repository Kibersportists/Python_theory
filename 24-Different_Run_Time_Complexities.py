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

n = int(input("Enter a number:"))
x = 0 # O(1)
for i in range(n): # worst case O(n), best case Ω(n), average case Θ(n) n <= average <= n
    print(i) # O(1)

# worst case  even number O(n), best case - odd number Ω(1), average case = 1 <= average <= n
if n % 2 == 0: # O(1)
    for i in range(n): # O(n)
        x += i # O(1)

# worst case  odd number (3*n) - O(n), best case - even number Ω(n), average case = n <= average <= 3n
# Ω(n) <= average <= O(n)
if n % 2 == 0: # O(1)
    for i in range(n): # O(n)
        x += i # O(1)
else:
    for i in range(n*3): # 3*n = O(n)
        x += i # O(1)



# TASK: Give worst, best and average case runtimes of the following code
n = int(input("Enter a number:"))
x = 0 # O(1)

# worst case even number (n*n) - O(n^2), best case - odd number (n*3) - Ω(n), 
# average case = 3n <= average <= n*n -> Ω(n) <= average <= O(n^2)
if n % 2 == 0: # O(1)
    for i in range(n*n): # O(n^2)
        x += i # O(1)
else:
    for i in range(n*3): # 3*n = O(n)
        x += i # O(1)





