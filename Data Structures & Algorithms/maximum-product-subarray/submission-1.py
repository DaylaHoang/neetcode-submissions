# Plan
# 1. Intialize current_max, current_min, result = nums[0]
# 2. For each next number
#       start a new subarray with the number itself
#       extend the previous maximum-product subarray
#       extend the previous minimum-product subarray
# 3. Update current_max and current_min using all 3 choices
# 4. Update the global result
# 5. Return result

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_max, current_min = nums[0], nums[0]
        result = nums[0]
        # Process each remaining number
        for num in nums[1:]:
            # 3 choices: start a new subarray with num, extend the previous maximum product, extend previous min product
            candidates = (num, current_max * num, current_min * num)
            # Update both values at the same time
            current_max = max(candidates)
            current_min = min(candidates)
            # Track the largest product found anywhere
            result = max(result, current_max)
        return result