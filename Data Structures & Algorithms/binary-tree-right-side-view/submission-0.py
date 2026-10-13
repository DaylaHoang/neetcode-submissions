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
        # An empty tree has no visible nodes
        if not root:
            return []

        result = []
        queue = deque([root])

        # Process the tree on level at a time
        while queue:
            # Fix the number of nodes in the current level
            level_size = len(queue)
            for i in range(level_size):
                # Remove the next node from the current node
                node = queue.popleft()

                # The last node is the rightmost node of this level
                if i == level_size - 1:
                    result.append(node.val)
                
                # Add children from left to right. They will be processed in the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result
        