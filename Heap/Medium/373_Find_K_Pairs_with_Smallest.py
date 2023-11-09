"""
    You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.
    Define a pair (u, v) which consists of one element from the first array and one element from the second array.
    Time O(k log(k))
    Space O(k)
"""


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        from heapq import heappush, heappop

        if not nums1 or not nums2:
            return []

        m = len(nums1)
        n = len(nums2)
        visited = set()
        minHeap = []
        ans = []

        heappush(minHeap, (nums1[0] + nums2[0], 0, 0))
        visited.add((0, 0))

        while k and minHeap:
            val, i, j = heappop(minHeap)
            ans.append([nums1[i], nums2[j]])
            if i + 1 < m and (i + 1, j) not in visited:
                heappush(minHeap, (nums1[i + 1] + nums2[j], i + 1, j))
                visited.add((i + 1, j))
            if j + 1 < n and (i, j + 1) not in visited:
                heappush(minHeap, (nums1[i] + nums2[j + 1], i, j + 1))
                visited.add((i, j + 1))
            k -= 1
        return ans
