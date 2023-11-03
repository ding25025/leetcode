"""
    Given the head of a sorted linked list, 
    delete all nodes that have duplicate numbers, 
    leaving only distinct numbers from the original list.
    Return the linked list sorted as well.
    Time O(n)
    Space O(1)
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None, None)
        # Set its next node as the head of the linked list
        dummy.next = head
        # Create a prev variable and initialize it with dummy
        prev = dummy
        cur = head
        while cur and cur.next:
            if cur.next.val == cur.val:
                # traverse the linked list and find all the duplicates
                while cur.next and cur.next.val == cur.val:
                    cur = cur.next
                cur.next, cur = None, cur.next
                prev.next = cur
            else:
                prev = cur
                cur = cur.next
        return dummy.next
