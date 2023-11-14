"""
    Given an integer array nums, return the length of the longest strictly increasing 
    subsequence.
    Time O(nlogn)
    Space O(N)

"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sub = [nums[0]]

        for num in nums:
            if num > sub[-1]:
                sub.append(num)
            else:
                # Use binary search to find the correct position to replace
                left, right = 0, len(sub) - 1
                while left < right:
                    mid = (left + right) // 2
                    if sub[mid] < num:
                        left = mid + 1
                    else:
                        right = mid
                sub[left] = num

        return len(sub)
