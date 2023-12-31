"""
    Given an array of integers nums and an integer target, 
    return indices of the two numbers such that they add up to target.
    Time: O(n)
    Space O(n)
    Tip: use hashmap,check for difference value 
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            # check difference value is exist in the hashmap
            if diff in result:
                return [result[diff], i]
            else:
                result[nums[i]] = i
