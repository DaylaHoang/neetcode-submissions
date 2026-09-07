class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Plan
        # 1. Treat nums as a linked list: next = nums[index]
        # 2. Use slow/fast pointers to find a meeting point in the cycle
        # 3. Reset slow to index 0
        # 4. Move both one step at a time
        # 5. Their meeting point is the duplicate

        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow