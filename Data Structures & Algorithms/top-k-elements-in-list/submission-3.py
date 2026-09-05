class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Bucket Sort
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            #count.items() returns pairs of key and value
            freq[cnt].append(num) ## put num in bucket freq[cnt]

        res = []
        for i in range(len(freq) - 1, 0, -1): ## from high freq → low
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res


