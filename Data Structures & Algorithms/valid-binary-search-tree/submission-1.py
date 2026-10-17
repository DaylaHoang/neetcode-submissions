# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Plan
# Start DFS with bounds (-inf, inf)
# If the node is None, return True
# If node.val <= lower or node.val >= upper, return False
# Recursively validate both subtrees with updated bounds

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, lower, upper):
            if not node: return True
            # The current value must be strictly within bounds
            if node.val <= lower or node.val >= upper:
                return False
            # Left values must be smaller than the current node
            left = dfs(node.left, lower, node.val)
            # Right balues must be larger than the current node
            right = dfs(node.right, node.val, upper)
            return left and right
        return dfs(root, float("-inf"), float("inf"))

        