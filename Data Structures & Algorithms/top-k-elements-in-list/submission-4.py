# Plan
# 1. Count the frequency of every number
# 2. Create buckets where bucket[i] contains numbers appreaing i times
# 3. Put each number into its frequency bucket
# 4. Traverse buckets from high frequency to low
# 5. Collect numbers until k elements are found then return result

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # A frequency can never be larger than the size of the input array ( < len(nums)) -> create bucket  
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res