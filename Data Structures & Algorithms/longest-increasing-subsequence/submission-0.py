# Plan
# 1. Initialize dp[i] = 1 for every index
# 2. Iterate i from left to right
# 3. For each i, check every previous index j < i
# 4. If nums[j] < nums[i]: dp[i] = max(dp[i], dp[j] + 1)
# 5. Return max(dp)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i] = length of the LIS ending at index i
        dp = [1] * n
        # Consider each number as the end of a subsequence
        for i in range(n):
            # Check all numbers before index i
            for j in range(i):
                # We can extend the subsequence only if nums[i] is larger
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1) # Extend the best subsequence ending at j
        return max(dp) # The LIS can end at any index