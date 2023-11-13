"""
    Given an integer array nums representing the amount of money of each house, 
    return the maximum amount of money you can rob tonight without alerting the police.
    Time O(n)
    Space O(1)
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2
