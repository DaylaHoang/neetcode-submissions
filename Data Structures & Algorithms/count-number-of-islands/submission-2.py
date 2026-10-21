# Plan
# 1. interate throug every cell
# 2. when we find "1", increment the island count
# 3. run interative DFS to mark all connected land as '0'
# 4. explore all 4 directions: up, down, left, right
# 5. return the count
# also note that we will use iterative DFS here because the grid can contain up to 10000 connected land cells, which may exceed Python's recursion limit

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "0":
                    continue
                islands += 1
                stack = [(row, col)]
                grid[row][col] = "0"

                while stack:
                    current_row, current_col = stack.pop()

                    for row_change, col_change in [
                        (1, 0), (-1, 0), (0, 1), (0, -1)
                    ]:
                        next_row = current_row + row_change
                        next_col = current_col + col_change
                        if (
                            0 <= next_row < rows
                            and 0 <= next_col < cols
                            and grid[next_row][next_col] == "1"
                        ):
                            grid[next_row][next_col] = "0"
                            stack.append((next_row, next_col))
        return islands