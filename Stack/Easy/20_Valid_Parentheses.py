"""
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
    determine if the input string is valid.
    Time O(N)
    Space O(N)
    
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {"(": ")", "{": "}", "[": "]"}
        for bracket in s:
            if bracket in pairs:
                stack.append(bracket)
            elif len(stack) == 0 or bracket != pairs[stack.pop()]:
                return False
        return len(stack) == 0
