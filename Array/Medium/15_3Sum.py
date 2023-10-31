"""
    Time - O(n2)
    Space - O(1) O(n)
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, ele in enumerate(nums):
            if i > 0 and ele == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                total = ele + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    res.append([ele, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res
