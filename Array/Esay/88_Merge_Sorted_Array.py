"""
    1.Given Two Sorted Array 
    2.Merge Array
    Time - O(m+n)
    Space - O(1)
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1  # nums1 pointer
        j = n - 1  # nums2 pointer
        k = m + n - 1
        while i >= 0 and j >= 0:
            # put into the last position
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                # nums2 is bigger than nums1
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
