'''
1. Define a DP hash map
    dp[sum] = number of ways to reach that sum
2. Initialize the base case
    dp = {0: 1}
3. Process each number
4. Return dp.get(target, 0)
'''

from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {0: 1}
        for num in nums:
            next_dp = defaultdict(int)
            for total, count in dp.items():
                next_dp[total + num] += count
                next_dp[total - num] += count
            dp = next_dp
        return dp.get(target, 0)
        