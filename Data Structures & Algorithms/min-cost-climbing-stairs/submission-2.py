# 1. Define dp[i] as the minumum cost to reach stair i
# 2. Initalize dp[0] = dp[1] = 0 because either is a valid starting point
# 3. For each stair from 2 through n, calculate the cheaper of arriving from previous stair or 2 stairs back
# 4. Return dp[n], which represents reaching the top
# 5. Optimize space because we only need the previous 2 DP values
# Note: dp[i] = min cost to reach step i, excluding price of step i
# Formula: dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev2, prev1 = 0, 0
        for i in range(2, len(cost) + 1):
            current = min(prev1 + cost[i-1], prev2 + cost[i-2])
            prev2 = prev1
            prev1 = current
        return prev1


