"""
    Given the root of a binary tree, 
    return the level order traversal of its nodes' values. 
    (i.e., from left to right, level by level).
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack = [root]
        result = []
        if root is None:
            return []

        while stack:
            lvl = []
            for i in range(len(stack)):
                node = stack.pop(0)
                lvl.append((node.val))

                if node.left:
                    stack.append(node.left)

                if node.right:
                    stack.append(node.right)
            result.append(lvl)
        return result
