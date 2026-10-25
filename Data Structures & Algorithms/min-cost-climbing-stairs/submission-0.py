# 1. Define dp[i] as the minumum cost to reach stair i
# 2. Initalize dp[0] = dp[1] = 0 because either is a valid starting point
# 3. For each stair from 2 through n, calculate the cheaper of arriving from previous stair or 2 stairs back
# 4. Return dp[n], which represents reaching the top
# 5. Optimize space because we only need the previous 2 DP values

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)

        for i in range(2, n + 1):
            one_step = dp[i - 1] + cost[i-1]
            two_steps = dp[i - 2] + cost[i - 2]
            dp[i] = min(one_step, two_steps)
        return dp[n]