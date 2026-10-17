# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Plan
# If root is None -> return [] -> empty tree has no visible nodes
# Initialize queue with root and result = [] -> BFS processes nodes level by level
# For each level:
# - Get the number of nodes in this level
# - Process all nodes from left to right
# - Add the last node's value to result
# Return result

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node, depth):
            if not node: return
            if depth == len(res):
                res.append(node.val)
            
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        dfs(root, 0)
        return res
