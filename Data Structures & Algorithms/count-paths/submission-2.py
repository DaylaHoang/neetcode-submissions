'''
State: dp[i][j] = number of unique paths to cell (i, j)
DP Recurrence: dp[i][j] = dp[i-1][j] + dp[i][j-1]
Base cases: dp[0][j] = 1 # First row: only move right
            dp[i][0] = 1 # First column: only move down

Plan
1. Define a 2D DP table: dp[i][j]
2. Initialize the base cases: dp[0][j] = 1 | dp[i][0] = 1
3. Fill the remaining cells using DP Recurrence
4. Return the destination
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m-1][n-1]