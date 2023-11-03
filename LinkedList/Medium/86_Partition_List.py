"""
    Given the head of a linked list and a value x, 
    partition it such that all nodes less than x come before nodes greater than or equal to x.
    Time O(n)
    Space O(1)
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        beforeNode = ListNode(0, None)
        afterNode = ListNode(0, None)
        before = beforeNode
        after = afterNode

        cur = head

        while cur:
            if cur.val < x:
                before.next = cur
                before = before.next
            else:
                after.next = cur
                after = after.next
            cur = cur.next

        before.next = afterNode.next
        after.next = None

        return beforeNode.next
