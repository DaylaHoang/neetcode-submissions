# Plan
# 1. Create 2 visited sets: pacific and atlantic
# 2. Define DFS that takes a cell and a visited set
# 3. Mark the current cell as visited
# 4. Explore 4 neighbors if they are inside the grid, unvisited, and at least as high as the current cell
# 5. Start Pacific DFS from the top and left borders
# 6. Start Atlantic DFS from the bottom and right borders
# 7. Return cells visited by both traversals

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        
        def dfs(row, col, visited):
            visited.add((row, col)) # Mark this cell as reachable from the ocean
            for row_change, col_change in [
                (1, 0), (-1, 0), (0, 1), (0, -1)
            ]:
                next_row = row + row_change
                next_col = col + col_change
                if (
                    0 <= next_row < rows
                    and 0 <= next_col < cols
                    and (next_row, next_col) not in visited
                    and heights[next_row][next_col] >= heights[row][col]
                ):
                    # Reverse DFS: move uphill to find cells that can drain to this ocean
                    dfs(next_row, next_col, visited)

        # Pacific: top and left borders
        for row in range(rows):
            dfs(row, 0, pacific)
        for col in range(cols):
            dfs(0, col, pacific)
        # Atlantic: bottom and right borders
        for row in range(rows):
            dfs(row, cols - 1, atlantic)
        for col in range(cols):
            dfs(rows - 1, col, atlantic)
        
        return [[row, col] for row, col in pacific & atlantic]
        