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

        if not head: return None

        old_to_new = {}

        cur = head
        while cur:
            node = Node(cur.val)
            old_to_new[cur] = node
            cur = cur.next
        
        cur = head
        while cur:
            copy = old_to_new[cur]
            copy.next = old_to_new[cur.next] if cur.next else None
            copy.random = old_to_new[cur.random] if cur.random else None
            cur = cur.next
        
        return old_to_new[head]

