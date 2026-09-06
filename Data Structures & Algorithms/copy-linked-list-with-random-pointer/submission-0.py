"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Plan
        # 1. Create a map: original node -> copied node
        # 2. Create all copied nodes in the pass
        # 3. Second pass: connect next and random using the map
        # 4. Return the copy of head

        node_map = {}

        current = head
        while current:
            node_map[current] = Node(current.val)
            current = current.next
        # Step 2 connect next and random pointers
        current = head
        while current:
            copied_node = node_map[current]
            copied_node.next = node_map.get(current.next)
            copied_node.random = node_map.get(current.random)
            current = current.next
        return node_map.get(head)


