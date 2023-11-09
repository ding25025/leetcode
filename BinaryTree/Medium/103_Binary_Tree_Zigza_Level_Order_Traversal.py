"""
    Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, 
    then right to left for the next level and alternate between).
    left->right
    right->left
    left->right
    ...

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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        q = deque([root])
        while q:
            level = []
            for node in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # even line and then reverse
            if len(ans) % 2:
                level = reversed(level)

            ans.append(level)
        return ans
