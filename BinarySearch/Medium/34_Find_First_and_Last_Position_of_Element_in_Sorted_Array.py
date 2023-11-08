"""
    Given an array of integers nums sorted in non-decreasing order, 
    find the starting and ending position of a given target value.
    If target is not found in the array, return [-1, -1].
    You must write an algorithm with O(log n) runtime complexity.

"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # O(n)
        # O(1)
        l = 0
        r = len(nums) - 1
        # while l<=r:
        #     if nums[l]<target:
        #        l+=1
        #     elif nums[r]>target:
        #         r-=1
        #     elif nums[l]==target and nums[r]==target:
        #         return [l,r]
        # return [-1,-1]

        # O(logN)
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                l = mid
                r = mid
                while l - 1 >= 0 and nums[l - 1] == target:
                    l -= 1
                while r + 1 < len(nums) and nums[r + 1] == target:
                    r += 1
                return [l, r]
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return [-1, -1]
