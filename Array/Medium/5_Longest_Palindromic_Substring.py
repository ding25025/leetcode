"""
    Given a string s, return the longest palindromic substring in s.
    ex: babad -> bab or aba
        cbbd -> bb
        a -> a
    Time O(n)
    Space O(m)    
    *Manacher
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
