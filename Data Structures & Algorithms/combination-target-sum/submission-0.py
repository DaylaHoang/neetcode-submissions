'''
1. Track the current combination and its total
2. If total == target, save a copy of the combination
3. If total > target or no numbers remain, stop
4. Include nums[i] and stay at i (allow reuse)
5. Backtrack and skip nums[i] by moving to index i + 1
'''
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result, curr = [], []
        def dfs(i, total):
            # Base case 1: found combination = target
            if total == target:
                result.append(curr.copy()) # Save copy to prevent pop() changes
                return
            # Base case 2: already checked all nums or out of bound
            if i == len(nums) or total > target:
                return
            # Choice 1: Take nums[i]
            curr.append(nums[i])
            dfs(i, total + nums[i])
            curr.pop()
            dfs(i + 1, total)
        dfs(0,0) # start at index 0, total = 0
        return result


        