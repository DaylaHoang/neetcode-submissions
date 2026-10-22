# 1. Count all fresh fruits
# 2. Add all rotten fruits to the queue
# 3. If there are no fresh fruits, return 0
# 4. Process BFS one level at a time
# 5. For each rotten fruit, inspect 4 neighbors
# 6. Turn fresh neighbors rotten, decrement the fresh count, and enqueue them
# 7. After each completed level that spreads infection, increment minutes
# 8. Return minutes if no fresh fruit remains; otherwise return -1

from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        minutes = 0

        # Find all rotten fruits and count fresh fruits
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh_count += 1
        # No fresh fruit means no time is needed
        if fresh_count == 0:
            return 0
        # Each BFS level represents one minute
        while queue and fresh_count > 0:
            # len(queue) doesn't know which is BFS level
            level_size = len(queue)
            for i in range(level_size):
                current_row, current_col = queue.popleft()
                for row_change, col_change in [
                    (1, 0), (-1, 0), (0, 1), (0, -1)
                ]:
                    next_row = current_row + row_change
                    next_col = current_col + col_change
                    if (
                        0 <= next_row < rows
                        and 0 <= next_col < cols
                        and grid[next_row][next_col] == 1
                    ):
                        grid[next_row][next_col] = 2
                        fresh_count -= 1
                        queue.append((next_row, next_col))
            minutes += 1
        return minutes if fresh_count == 0 else -1
        