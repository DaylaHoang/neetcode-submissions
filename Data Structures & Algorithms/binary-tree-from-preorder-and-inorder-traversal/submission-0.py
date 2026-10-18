# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Plan
# 1. Build a hashmap of each value's position in inorder
# 2. Maintain preorder_index to indentify the next root
# 3. Define dfs(left, right) to build the subtree within those inorder boundaries
# 4. Create the root, recursively build its left subtree, then its right subtree
# 5. Return the reconstructed root

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Map each value to its postion in inorder
        inorder_index = {value: i for i, value in enumerate(inorder)}
        preorder_index = 0
        
        def dfs(left, right):
            nonlocal preorder_index
            # No values remain in this subtree
            if left > right:
                return None
            # The next preorder value is the subtree's root
            root_value = preorder[preorder_index]
            preorder_index += 1
            root = TreeNode(root_value)
            # Find the root's position in inorder
            mid = inorder_index[root_value]
            # Build left first, then right (preorder order)
            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)
            return root
        return dfs(0, len(inorder) - 1)
        