"""
    A valid BST is defined as follows:
    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.
    Time O(N)
    Space O(N)
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # root left right

        def BST(root, min_val, max_val):
            if root is None:
                return True

            if min_val < root.val < max_val:
                left = BST(root.left, min_val, root.val)
                right = BST(root.right, root.val, max_val)
                return left and right
            else:
                return False

        return BST(root, float("-inf"), float("inf"))
