"""
Given an integer array nums sorted in non-decreasing order, 
remove the duplicates **in-place** such that each unique element appears only once. 
The relative order of the elements should be kept the same. 
Then return the number of unique elements in nums.
Time - O(n)
Space - O(1)
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        while i <= j and j < len(nums):
            if nums[i] == nums[j]:
                j += 1
            else:
                nums[i + 1] = nums[j]
                i += 1
        return i + 1
