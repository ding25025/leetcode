"""
    You are climbing a staircase. It takes n steps to reach the top.

    Each time you can either climb 1 or 2 steps. 
    In how many distinct ways can you climb to the top?
    Time O(n)
    Space O(1)
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for _ in range(n - 1):
            temp = one + two
            one = two
            two = temp
        return two
