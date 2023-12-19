"""
    Given the head of a linked list,
    remove the nth node from the end of the list and return its head.
    Time O(n)
    Space O(1)
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        count = 0
        #calculate nodes
        while curr:
            curr = curr.next
            count += 1

        check = count - n - 1
        count = 0
        curr = head
        # return the last node
        if check == -1:
            return head.next

        while curr:
            if count == check:
                curr.next = curr.next.next
                break
            curr = curr.next
            count += 1

        return head
