# problem_solutions.py

def twoSum(nums, target):
    """
    Given an array of integers `nums` and an integer `target`,
    return indices of the two numbers such that they add up to target.
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def isValid(s):
    """
    Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']',
    determine if the input string is valid.
    """
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:
            return False
    return not stack
