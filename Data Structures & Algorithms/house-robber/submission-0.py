# Plan
# 1. State: dp[i] = maximum money we can rob from houses 0 to i
# 2. At each house, either rib it or skip it
# 3. Recurrence: dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
# 4. Base case: start with 2 previous DP values = 0
# 4. Optimization: Keep only two_houses_back and one_house_back instead of a DP array
# Return one_house_back after processing all house
# Time O(n) | Space O(1)

class Solution:
    def rob(self, nums: List[int]) -> int:
        two_houses_back = 0 # Best amount before the previous house
        one_house_back = 0 # Best amount through the previous house
        for money in nums:
            skip = one_house_back # Option 1: skip the house
            rob = two_houses_back + money # Option2: rob this house
            current = max(skip, rob)
            # move forward to the next house
            two_houses_back = one_house_back
            one_house_back = current
        return one_house_back