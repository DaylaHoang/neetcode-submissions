# Plan
# Intitialze dp = [1] * n
# For each r from 1 to m - 1:
#           for each c from 1 to n - 1:
# update dp[c] += dp[c - 1]
# return dp[n - 1]

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0
        dp = [1] * n
        for r in range(1, m):
            for c in range(1, n):
                dp[c] = dp[c] + dp[c - 1]
        return dp[n-1]