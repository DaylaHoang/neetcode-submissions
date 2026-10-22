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
        # map each original node to its cloned node
        clones = {node: Node(node.val)}
        queue = deque([node])
        while queue:
            current_node = queue.popleft()
            for neighbor in current_node.neighbors:
                # Create a clone if we haven't seen this node
                if neighbor not in clones:
                    clones[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                    # Connect the cloned nodes
                clones[current_node].neighbors.append(clones[neighbor])
        return clones[node]
        