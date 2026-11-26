'''
1. Sort candidates to group duplicate values
2. Save a copy when total == target
3. Stop when total exceeds target or index is out of bounds
4. Include the current number and move to i + 1
5. Back track, skip duplicates, and explore the exclusion branch
'''

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result, curr = [], []
        def dfs(i, total):
            if total == target:
                result.append(curr.copy())
                return
            if i == len(candidates) or total > target:
                return
            # Ban đầu cho phép lấy nhiều số duplicate ở các index khác nhau
            curr.append(candidates[i])
            dfs(i + 1, total + candidates[i])
            curr.pop()

            # Chỉ skip duplicate khi thử nhánh k lấy
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            dfs(i + 1, total)
        dfs(0,0)
        return result