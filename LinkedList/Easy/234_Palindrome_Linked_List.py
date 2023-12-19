"""
    Given the head of a singly linked list, return true if it is a 
    palindrome or false otherwise.
    ex:[1,2,2,1] =>True  [1,2]=>False
    Tip: use stack

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        curr = head

        while curr:
            stack.append(curr.val)
            curr = curr.next

        curr = head

        while curr:
            if curr.val != stack.pop():
                return False
            curr = curr.next
        return True
