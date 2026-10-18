# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Plan
# 1. Use iterative inorder traversal with a stack
# 2. Keep moving left, pushing nodes onto the stack
# 3. Pop a node, decrement k, and check whether k == 0
# 4. If not, move to its right subtree and repeat

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        current = root
        while current or stack:
            # Visit the leftmost nodes first
            while current:
                stack.append(current)
                current = current.left
            # Process the next smallest node
            current = stack.pop()
            k -= 1
            if k == 0:
                return current.val
            # Then explore the right subtree
            current = current.right
        