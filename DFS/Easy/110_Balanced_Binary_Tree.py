"""
    Given a binary tree, determine if it is 
    height-balanced.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # first
        # check left and right  is <=1
        def dfs(root):
            if root is None:
                return [True, 0]

            left = dfs(root.left)
            right = dfs(root.right)
            balance = left[0] and right[0] and abs(left[1] - right[1] <= 1)
            return [balance, 1 + max(left[1], right[1])]

        result = dfs(root)
        return result[0]
