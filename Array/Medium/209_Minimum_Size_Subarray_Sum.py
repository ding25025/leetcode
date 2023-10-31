"""
    Given an array of positive integers nums and a positive integer target, 
    return the minimal length of a subarray whose sum is greater than or equal to target. 
    If there is no such subarray, return 0 instead.
    Time - O(n)
    Space - O(1)
"""


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0

        total = 0
        left = 0
        min_len = float("inf")
        n = len(nums)

        for r in range(n):
            total += nums[r]
            while total >= target:
                min_len = min(r - left + 1, min_len)
                total -= nums[left]
                left += 1
        return 0 if min_len == float("inf") else min_len
