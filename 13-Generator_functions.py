''' Problem 1 '''
def func():
    return 5
    return 10

print(func())


''' Problem 2 '''
def gen_func():
    yield 5         #1st iteration
    yield 10        #2nd iteration
    yield "Python"  #3rd iteration
    yield 100       #4th iteration

# lst = [elem for elem in gen_func()]
lst = list(gen_func())
print(lst)


''' Problem 3 '''
def twos_power(n):
    total = 1
    while n >= 0:
        yield total
        total *= 2
        n -= 1

lst = list(twos_power(5))
print(lst)


''' Problem 4 
Why is it that we can write the following?
for elem in lst:
    print(elem)
Because built into the list class, there is a generator function allows us to!
'''
def iter_lst(lst):
    for i in range(len(lst)):
        yield lst[i]

lst = [10, 12, 40, "Python"]

for elem in iter_lst(lst):
    print(elem)


''' Problem 5 
Is Range a generator function then? No!
But, we can use a generator function to create something similar!
'''
# for i in range(1, 10, 1):
#     print(i)

def my_range(start, stop, step):
    while start < stop:
        yield start
        start += step

for i in my_range(1, 10, 1):
    print(i)

lst = list(my_range(1, 10, 1))
print(lst)



