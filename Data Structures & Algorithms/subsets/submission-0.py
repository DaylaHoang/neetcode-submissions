'''
1. Track the current subset and index i
2. If i == n, save a copy, all decisions are complete
3. Include nums[i], then explore the remaining numbers
4. Remove it to undo that chice
5. Skip nums[i], then explore the remaining numbers
'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result, subset = [], []
        def dfs(i):
            if i == len(nums):
                result.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)
        dfs(0)
        return result