'''
1. Maintain a curent permutation and a set of used numbers
2. If the permutation contains all numbers, save a copy
3. Iterate through all numbers and skip those already used
4. Choose an unused number and recursively explore
5. Undo the choice to explore other possibilities
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result, curr = [], []
        used = set() # Track numbers already selected

        def dfs():
            # Base case: all numbers have been selected
            if len(curr) == len(nums):
                result.append(curr.copy())
                return # Finished this brand and return to parent
            for num in nums:
                if num in used:
                    continue # skip numbers already in curr
                curr.append(num)
                used.add(num)
                dfs()
                curr.pop()
                used.remove(num)
        dfs()
        return result

