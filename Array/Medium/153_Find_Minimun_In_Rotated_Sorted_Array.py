"""
    Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
    Time - O(logN)
    Space - O(1)
"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                # move to left side
                right = mid
            else:
                # move right side
                left = mid + 1
        return nums[right]
