"""
    Given an array of characters chars, compress it using the following algorithm
    chars = ["a","a","b","b","c","c","c"] => ["a","2","b","2","c","3"]
    chars = ["a"] => ["a"]
    Time: O(n)
    Space O(1)
"""


class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        ans = 0

        while i < len(chars):
            letter = chars[i]
            count = 0
            while i < len(chars) and chars[i] == letter:
                count += 1
                i += 1
            chars[ans] = letter
            ans += 1
            if count > 1:
                for c in str(count):
                    chars[ans] = c
                    ans += 1
        return ans
