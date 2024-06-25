"""
    Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, 
    return the k closest points to the origin (0, 0).
    Time:
    Space:
"""

from heapq import heapify, heappop, heappush


class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        minHeap = []
        # calculate distance and insert to minHeap
        for x, y in points:
            dist = x**2 + y**2
            heappush(minHeap, [dist, x, y])

        heapify(minHeap)

        result = []
        # select k nearest dist
        while k > 0:
            dist, x, y = heappop(minHeap)
            result.append([x, y])
            k -= 1
        return result
