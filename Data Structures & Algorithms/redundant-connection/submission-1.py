

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))
        size = [1] * (n + 1)
        def find(node):
            # Find the representative of this node's group
            if parent[node] != node:
                parent[node] = find(parent[node]) # Path compression
            return parent[node]
        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)
            # Already connected: this edge creates a cycle
            if root1 == root2:
                return False
            # Attach the smaller group to the larger group
            if size[root1] < size[root2]:
                root1, root2 = root2, root1
            parent[root2] = root1
            size[root1] += size[root2]
            return True
        for node1, node2 in edges:
            if not union(node1, node2):
                return [node1, node2]
        return []
        