"""
    You are given a string s and an array of strings words. 
    All the strings of words are of the same length.
    A concatenated substring in s is a substring that contains all the strings of any permutation of words concatenated.
"""
from collections import Counter, defaultdict


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        length = len(words[0])
        hmap = Counter(words)
        res = []
        for i in range(length):
            start = i
            window = defaultdict(int)
            words_used = 0

            for j in range(i, len(s) - length + 1, length):
                word = s[j : j + length]

                if word not in hmap:
                    # move to next word
                    start = j + length
                    window = defaultdict(int)
                    words_used = 0
                    continue
                words_used += 1
                window[word] += 1

                while window[word] > hmap[word]:
                    window[s[start : start + length]] -= 1
                    start += length
                    words_used -= 1

                if words_used == len(words):
                    res.append(start)
        return res
