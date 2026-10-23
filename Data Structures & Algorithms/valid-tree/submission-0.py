# Plan
# 1. Check that the grpah has exactly n - 1 edges
# 2. Build an ajancency list for the undirected graph
# 3. Run DFS starting from node 0
# 4. Track visited nodes using a set
# 5. Return whether DFS visited all n nodes

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        graph = [[] for i in range(n)]
        # Undirected prah: connect both directions
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        visited = set()
        
        def dfs(node):
            if node in visited:
                return False
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)
        dfs(0)
        return len(visited) == n