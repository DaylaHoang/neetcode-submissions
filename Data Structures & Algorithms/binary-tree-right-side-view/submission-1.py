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

        #Process the tree one level at a time
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft() #pop the next node from the current level
                if i == level_size - 1:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result
