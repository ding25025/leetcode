"""
    Given the head of a linked list, 
    rotate the list to the right by k places.
    Time O(n)
    Space O(1)
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        if k == 0:
            return head
        length = 1
        last = head
        while last.next:
            last = last.next
            length += 1
        print(length)
        k = k % length

        print(k)
        # point to head
        last.next = head

        temp = head
        for _ in range(length - k - 1):
            temp = temp.next

        res = temp.next
        temp.next = None

        return res
