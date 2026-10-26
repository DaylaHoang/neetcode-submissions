# Plan
# Edge cases: if there's only 1 house, return its value
# Helper: rob_linear(houses) computes the maximum money for a straight line of houses
# State: maintain two_houses_back and one_house_back
# Recurrence: current = max(one_house_back, tow_houses_back + money)
# Case 1: rob houses nums[:-1] (exlude last)
# Case 2: rob houses nums[1:] (exclude first)
# Return: max of the 2 cases
# Time O(n) | Space O(1)

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
         # A single house
        if n == 1:
            return nums[0]
 
        def rob_linear(start, end):
            two_houses_back = 0
            one_house_back = 0
            for index in range(start, end):
                money = nums[index]
                current = max(one_house_back, two_houses_back + money)
                two_houses_back = one_house_back
                one_house_back = current
            return one_house_back

        exclude_last = rob_linear(0, n - 1)
        exclude_first = rob_linear(1, n)

        return max(exclude_last, exclude_first)