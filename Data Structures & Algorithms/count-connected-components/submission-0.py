# Plan
# 1. Build an undirected adjacency list
# 2. Create a visited set and initialize components = 0
# 3. Iterate through every node
# 4. If the node is unvisited, increment components and run DFS to mark its entire connected groups
# 5. Return components

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for i in range(n)]
        # Build undirected graph
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        visited = set()
        components = 0
        def dfs(node):
            if node in visited:
                return False
            visited.add(node) # Mark this node as visited
            for neighbor in graph[node]:
                dfs(neighbor) # Explore all connected nodes
        for node in range(n):
            if node not in visited:
                components += 1 # Found a new component
                dfs(node) # Mark its entire group as visited
        return components
        