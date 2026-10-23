# Plan
# 1. Define DFS to mark connected 0 cells as S
# 2. Start DFS from all four borders
# 3. Scan the entire board
# 4. Convert remaining 0 to X, and S back to 0
# note: using iteratie DFS to prevent recursion depth when board is as large as 200x200

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        def dfs(row, col):
            stack = [(row, col)]
            board[row][col] = "S" # Mark border-connected 0 as safe
            while stack:
                row, col = stack.pop() # Explore one cell
                for row_change, col_change in [
                    (1, 0), (-1, 0), (0, 1), (0, -1)
                ]:
                    next_row = row + row_change
                    next_col = col + col_change
                    if (
                        0 <= next_row < rows
                        and 0 <= next_col < cols
                        and board[next_row][next_col] == "O"
                    ):
                        board[next_row][next_col] = "S"
                        stack.append((next_row, next_col))
    # 1. Start DFS from all four borders
        for row in range(rows):
            if board[row][0] == "O":
                dfs(row, 0) # check left
            if board[row][cols - 1] == "O":
                dfs(row, cols - 1) # check right
                
        for col in range(cols):
            if board[0][col] == "O":
                dfs(0, col) # check top
            if board[rows - 1][col] == "O":
                dfs(rows - 1, col) # check bottom

        # 2. Capture surrounded 0's and restore safe cells
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "S":
                    board[row][col] = "O"