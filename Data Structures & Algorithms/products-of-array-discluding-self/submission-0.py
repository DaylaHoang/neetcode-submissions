class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res  = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res        




        '''
        Solution if we can use division operation:

        total = 1
        for n in nums:
            total *= n
        
        res = []
        for n in nums:
            res.append(total // n)
        return res
        '''