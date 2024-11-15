# Algorithm Challenge - Sorting and Searching:
# Write a Python function to implement binary search on a sorted list of integers.
# The function should take a list and a target value as input and return the index of the target value in the list.
# If the target value is not found, return -1. Avoid using built-in search functions.

def binary_search(sorted_list, target):
    """
    Perform binary search on a sorted list to find the target value.
    
    :param sorted_list: A sorted list of integers.
    :param target: The integer value to search for.
    :return: Index of the target value or -1 if not found.
    """
    left, right = 0, len(sorted_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example usage:
nums = [1, 3, 5, 7, 9, 11, 13]
target = 7
print(binary_search(nums, target))  # Output: 3
