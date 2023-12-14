from typing import List


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


if __name__ == "__main__":
    sol = Solution()
    nums = [2, 1, 5, 3]
    print(sol.twoSum(nums, 4))
