# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Plan
        # If subRoot is None -> True
        # If root is None -> False
        # If root and subRoot match -> compare entire trees
        # Otherwise, search root.left and root.right

        def sameTree(p, q):
            if not p and not q:
                return True
            if (p and not q) or (q and not p):
                return False
            if p.val != q.val:
                return False
            return sameTree(p.left, q.left) and sameTree(p.right, q.right)

        def has_subtree(root):
            if not root:
                return False
            if sameTree(root, subRoot):
                return True
            return has_subtree(root.left) or has_subtree(root.right)
        return has_subtree(root)