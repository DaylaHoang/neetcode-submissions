'''
1. Sort intervals by starting time
2. Initialize res with the first interval
3. Interate through remaining intervals:
    if current.start > res[-1].end:
        append current (no overlap)
    otherwise: update res[-1].end with max end (merge)
4. Return res
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        for interval in intervals[1:]:
            if interval[0] > res[-1][1]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res