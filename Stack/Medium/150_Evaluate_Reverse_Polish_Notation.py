"""
    You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
    Evaluate the expression. Return an integer that represents the value of the expression.
    Time O(n)
    Space O(n)
"""


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = ["+", "-", "*", "/"]
        for val in tokens:
            if val in op:
                x, y = int(stack.pop()), int(stack.pop())
                cal = 0
                if val == "+":
                    cal = y + x
                if val == "-":
                    cal = y - x
                if val == "*":
                    cal = y * x
                if val == "/":
                    cal = y / x
                stack.append(cal)
            else:
                stack.append(val)
        return int(stack[-1])
