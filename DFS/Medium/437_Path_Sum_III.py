"""
    Given the root of a binary tree and an integer targetSum, 
    return the number of paths where the sum of the values along the path equals targetSum.
    Time O(n)
    Space O(1)
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        result = 0

        def dfs(node, target):
            if node is None:
                return
            find_path_from_node(node, target)
            dfs(node.left, target)
            dfs(node.right, target)

        def find_path_from_node(node, target):
            nonlocal result
            if node is None:
                return
            if node.val == target:
                result += 1
            find_path_from_node(node.left, target - node.val)
            find_path_from_node(node.right, target - node.val)

        dfs(root, targetSum)

        return result
