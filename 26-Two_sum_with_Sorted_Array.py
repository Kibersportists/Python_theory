'''
Write a function where, given a sorted list of integers and a target integer number

if there are two distinct numbers in the sorted list that can add up to the target, return true
otherwise, false

Input: numbers = [2, 7, 11, 15, 20, 21], target = 9
Output: True because 2 + 7 == 9

Input: numbers = [2, 7, 11, 15, 19, 20, 21], target = 26
Output: True because 11 + 15 == 26, and also 7 + 19 == 26

Input: numbers = [2, 7, 11, 15, 20, 21], target = 12
Output: False, no two numbers add up to 12

'''

# def two_sum(numbers: list, target: int):
#     Output = False
#     True_string = "True because "
#     lst_copy = lst.copy()
#     for indx in range(len(lst) - 1):
#         lst_copy.pop(0)
#         for integer_2 in lst_copy:
#             if lst[indx] + integer_2 == target:
#                 True_string += (str(lst[indx]) + " + " + str(integer_2) + " == " + str(lst[indx] + integer_2)) if not Output else (", and also " + str(lst[indx]) + " + " + str(integer_2) + " == " + str(lst[indx] + integer_2))
#                 Output = True
#     return True_string if Output else "False, no two numbers add up to 12"

def two_sum(numbers: list, target: int) -> bool:
    left = 0
    right = len(numbers) - 1

    while left < right:
        curr_sum = numbers[left] + numbers [right]
        if (curr_sum == target):
            return True
        elif (curr_sum < target):
            left += 1
        elif (curr_sum > target):
            right -= 1
    
    return False

lst = [2, 7, 11, 15, 19, 20, 21]

print("Test 1: ", two_sum(lst, 9))
print("Test 2: ", two_sum(lst, 26))
print("Test 3: ", two_sum(lst, 12))








