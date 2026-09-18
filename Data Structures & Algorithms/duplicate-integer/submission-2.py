class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
'''
sorting
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] = nums[i-1]:
                return True
        return False
Time comflexity: O(nlogn)
Space complexity: O(n)

'''

'''
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
'''