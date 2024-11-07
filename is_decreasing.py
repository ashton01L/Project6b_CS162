# Author: Ashton Lee
# Github User: ashton01L
# Date: 11/6/2024
# Description:Write a recursive function named is_decreasing that takes as its parameter a list of numbers.
def is_decreasing(numbers, index=1):
    """
    Recursively checks if a list of numbers is strictly decreasing.

    :param:
        numbers (list): A list of numbers.
        index (int, optional): The current index in the recursive call, starting at 1. Default is 1 to compare the
            first two elements.

    :return:
        bool: True if the list is strictly decreasing, False otherwise.
    """
    # Base case: if we have reached the end of the list, it is strictly decreasing
    if index == len(numbers):
        return True

    # Check if the current element is less than the previous one
    if numbers[index] >= numbers[index - 1]:
        return False

    # Recursive call to check the next element
    return is_decreasing(numbers, index + 1)
