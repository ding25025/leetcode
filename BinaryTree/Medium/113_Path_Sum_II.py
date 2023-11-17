"""
    Given the root of a binary tree and an integer targetSum, 
    return all root-to-leaf paths where the sum of the node values in the path equals targetSum. 
    Each path should be returned as a list of the node values, not node references.
    # Time O(n)
    # Space O(n)
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def dfs(path, root):
            if root:
                if not root.left and not root.right:
                    path.append(root.val)
                    if sum(path) == targetSum:
                        res.append(path)
                dfs(path + [root.val], root.left)
                dfs(path + [root.val], root.right)

        dfs([], root)

        return res
