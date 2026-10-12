# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Plan:
# Start at root
# If both p and q are smaller than root -> move left because nodes must be in the left subtree
# If both are larger -> move right
# Otherwise -> return current node -> this is where their paths meet/split

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        current = root

        while current:
            #Both nodes are smaller, so they must be on the left
            if p.val < current.val and q.val < current.val:
                current = current.left
            # Otherise, on the right
            elif p.val > current.val and q.val > current.val:
                current = current.right
            else:
                # They split here, or current equals p or q
                # This is the lowest common ancestor
                return current
        