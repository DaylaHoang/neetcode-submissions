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

        if not subRoot:
            return True
        
        if not root:
            return False
        
        if self.isSametree(root, subRoot):
            return True
        
        return (
            self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )

    def isSametree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return (
            self.isSametree(p.left, q.left)
            and self.isSametree(p.right, q.right)
        )