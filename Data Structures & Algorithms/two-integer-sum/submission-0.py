class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map = {} # Store values and indexes of each number

        for i, n in enumerate(nums):
            diff = target - n
            if diff in Map:
                return [Map[diff], i]
            Map[n] = i
        