"""
    Given an integer array nums, 
    return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        # left to right result
        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]

        right = nums[-1]
        # right to left result
        for i in range(len(nums) - 2, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res
