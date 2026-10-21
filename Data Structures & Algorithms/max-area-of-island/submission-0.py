# Plan
# 1. max_area = 0 - track the largest island found
# 2. Scan each cell using 2 for loops
# 3. If the cell is land, start BFS with area = 0
# 4. Use a deque to store discovered cells
# 5. For each removed cell, increment area and inspect 4 neighbors
# 6. Mark discovered land as 0 before enqueueing it
# 7. When BFS finsished, update max_area

from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area = 0

        # Scan every cell to discover new islands
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    continue
                # Start BFS for a new island
                area = 0
                queue = deque([(row, col)])
                grid[row][col] = 0

                while queue:
                    # Process one discovered land cell
                    current_row, current_col = queue.popleft()
                    area += 1
                    for row_change, col_change in [
                        (1, 0), (-1, 0), (0, 1), (0, -1)
                    ]:
                        next_row = current_row + row_change
                        next_col = current_col + col_change
                        # Only explore valid, unvisited land
                        if (
                            0 <= next_row < rows
                            and 0 <= next_col < cols
                            and grid[next_row][next_col] == 1
                        ):
                            grid[next_row][next_col] = 0
                            queue.append((next_row, next_col))
                max_area = max(max_area, area)
        return max_area