# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # DFS returns: height -> if balanced, -1 if unbalanced
        # Plan
        # DFS returns subtree height, or -1 if unbalanced
        # Recursively get left, right heights
        # If either is -1, propagate -1
        # If height > 1, return -1
        # Otherwise, return 1 + max(left, right)

        def dfs(node):
            if not node: return 0
            left_height = dfs(node.left)
            if left_height == -1:
                return -1

            right_height = dfs(node.right)
            if right_height == -1:
                return -1

            if abs(left_height - right_height) > 1:
                return -1

            return 1 + max(left_height, right_height)

        return dfs(root) != -1            