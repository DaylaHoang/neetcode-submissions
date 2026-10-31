# Plan
# Initialize: max_reach = 0 | last = len(nums) - 1
# For each index i, if i > max_reach: return False
# Update: max_reach = max(max_reach, i + nums[i])
# If max_reach >= last: return True, otherwise, return False after the loop


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        last = len(nums) - 1
        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
            if max_reach >= last:
                return True
        return False