# Plan
# 1. Intialize dp = [1] * n
# 2. For each row r from 1 to m-1:
#       for each column c from 1 to n-1
# 3. Update dp[c] += dp[c - 1]
# 4. Return dp[n-1]

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0
        dp = [1] * n
        for r in range(1, m):
            for c in range(1, n)  :
                dp[c] = dp[c] + dp[c - 1]
        return dp[n-1]      