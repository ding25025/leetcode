"""
    You are given the root of a binary tree containing digits from 0 to 9 only.
    Return the total sum of all root-to-leaf numbers. 
    Test cases are generated so that the answer will fit in a 32-bit integer.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # Time O(n)
        # Space O(n)

        def sumPath(node, path_sum):
            if node is None:
                return 0

            path_sum = 10 * path_sum + node.val

            if node.left is None and node.right is None:
                return path_sum

            return sumPath(node.left, path_sum) + sumPath(node.right, path_sum)

        return sumPath(root, 0)

    # stack solution
    # sum=0
    # stack=[(root,root.val)]
    # while stack:
    #     curr,value=stack.pop()
    #     if curr.left:
    #         left_value=10*value+curr.left.val
    #         stack.append((curr.left,left_value))
    #     if curr.right:
    #         right_value=10*value+curr.right.val
    #         stack.append((curr.right,right_value))

    #     if curr.left is None and curr.right is None:
    #         return  sum+=value
    # return sum
