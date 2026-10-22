"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# 1. Handle an empty graph
# 2. Create a clone of the starting node
# 3. Store original -> clone in a dictionary
# 4. Initialize a BFS queue with the starting node
# 5. For each original node, inspect its neighbor
# 6. Clone unseen neighbors and enqueue them
# 7. Connect the current cloned node to each cloned neighbor
# 8. Return the cloned starting node

from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        clones = {}
        def dfs(current_node):
            if current_node in clones:
                return clones[current_node]
            copy = Node(current_node.val)
            clones[current_node] = copy
            for neighbor in current_node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy
        return dfs(node)

    # Let V is vertices (nodes) and E the number of edges
    # Time: O(V + E)
    # Space O(V)
        