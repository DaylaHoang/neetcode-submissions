# Plan
# 1. Create a queue
# 2. Scan the grid and enqueue all treasure cells (0)
# 3. While the queue isn't empty, remove one cell
# 4. Check its four neighbors
# 5. If a neighbor is INF, set its distance to current_distance + 1
# 6. Enqueue that neighbor to continue BFS
# 7. Stop when the queue becomes empty

from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        INF = 2147483647
        queue = deque()

        # Start BFS from every treasure ches, scan the whole grid
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    queue.append((row, col))
        # Expand outward from all treasures
        while queue:
            current_row, current_col = queue.popleft()
            for row_change, col_change in [
                (1, 0), (-1, 0), (0, 1), (0, -1)
            ]:
                next_row = current_row + row_change
                next_col = current_col + col_change

                # Only visit land that has not been reached
                if (
                    0 <= next_row < rows
                    and 0 <= next_col < cols
                    and grid[next_row][next_col] == INF
                ):
                    grid[next_row][next_col] = (
                        grid[current_row][current_col] + 1
                    )
                    queue.append((next_row, next_col))

        