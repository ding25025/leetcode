"""
    Given a string s, find the length of the longest substring without repeating characters.
    ex: 
    Input: s = "abcabcbb"
    Output: 3
    Input: s = "bbbbb"
    Output: 1
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        seen = {}  # check string is exist or not
        start = 0
        ans = 0

        for i, c in range(len(s)):
            if c in seen:
                # update start index
                start = max(start, seen[c] + 1)
            # save character's index
            seen[c] = i
            # save maximun length
            ans = max(ans, i - start + 1)
            # because index is from zero, so add 1
        return ans
