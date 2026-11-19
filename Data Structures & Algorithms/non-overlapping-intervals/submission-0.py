'''
1. Sort intervals by start time. Process intervals from left to right
2. Initialize res = 0, prevEnd = intervals[0][1]
3. Iterate through remaining interval:
    if start >= prevEnd:
        update prevEnd (no overall)
    otherwise:
        res += 1
        prevEnd = min(prevEnd, end)
4. Return res
'''
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        res = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(prevEnd, end)
        return res
        