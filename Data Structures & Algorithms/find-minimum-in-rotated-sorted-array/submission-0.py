class Solution:
    def findMin(self, nums: List[int]) -> int:
        # example nums[1,2,3,4,5,6]
        # rotated: nums[3,4,5,6,1,2] -> min is 1
        l , r = 0, len(nums) - 1

        while l < r:
            m = l + (r - l) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else: r = m
        return nums[l]