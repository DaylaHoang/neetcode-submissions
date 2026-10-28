class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        # Equal subsets are impossible if the total is odd
        if total % 2 != 0:
            return False
        target = total // 2
        # dp[s] = True if we can form sum s
        dp = [False] * (target + 1)
        dp[0] = True # Choosing no numbers gives sum 0
        for num in nums:
            # Go backward to use each number only once
            for current_sum in range(target, num -1, -1):
                # Skip num OR take num if the remaining sum is achievable
                dp[current_sum] = (dp[current_sum] or dp[current_sum - num])

        return dp[target]