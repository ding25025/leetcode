"""
    Given an array of integers nums and an integer target, 
    return indices of the two numbers such that they add up to target.
    Time: O(n)
    Space O(n)
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in res:
                return [res[diff], i]
            else:
                res[nums[i]] = i
