# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Plan
# 1. DFS(node, max_so_far): track the maximum value along the current path
# 2. Base case: return 0 if the node is null
# 3. Check current node: count 1 if its value is at least max_so_far; otherwise count 
# 4. Recurse: update the maximum, count good nodes in both subtrees, and return the total

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_so_far):
            #No node means no good nodes to count, base case
            if not node: 
                return 0
            # Count the current node if it is good
            good = 1 if node.val >= max_so_far else 0
            # Update the maxium along this path
            max_so_far = max(max_so_far, node.val)
            # Count good nodes in both subtrees
            left = dfs(node.left, max_so_far)
            right = dfs(node.right, max_so_far)
            # Combine the current node and both subtrees
            return good + left + right
        return dfs(root, root.val)
        