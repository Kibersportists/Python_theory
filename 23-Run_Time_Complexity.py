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

x = 5 # Constant O(1)
y = 10 # Constant O(1)
z = x + y # Constant O(1)

print(1) # Constant O(1)
print(2) # Constant O(1)
print(3) # Constant O(1)

n = int(input("Enter a number:"))
for i in range(1, n + 1): # O(n) Linear
    print(i) # O(1)


m = int(input("Enter a number:"))
print("Here: " + str(m//2))
for i in range(1, m//2 + 1): # O(n) Quadratic
    print(i) # O(1)



# TASK: Analyze the worst case runtime per function
def func1(n): # Quadratic O(1 + (n^2 - 1)) -> O(n^2)
    x = 0 # 1
    for i in range (n*n): # n^2
        x += 1 # 1

def func2(n): # Linear O(1 + (n/2 -1)) -> O(n)
    y = 0 # 1
    for y in range (n//2): # n/2
        x += 1 # 1

def func3(n): # Quadratic O(1 + (n^2 - 1) + (n/2 -1)) -> O(n^2)
    z = 0 # 1
    for i in range (n**n): # n^2
        z += 1 # 1
    
    for i in range(n//2): # n/2
        z += 1 # 1








