"""
    Given an array nums of size n, return the majority element.
    The majority element is the element that appears more than ⌊n / 2⌋ times. 
    You may assume that the majority element always exists in the array.
    Time O(n)
    Space O(1)
    **Moore's Voting Algorithm**
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        result = 0
        for i in nums:
            if count == 0:
                result = i
            if i == result:
                count += 1
            else:
                count -= 1

        return result
