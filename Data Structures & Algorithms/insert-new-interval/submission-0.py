'''
1. initialize result = []
2. iterate through each interval:
    if completely on the left: append interval to result
    if completely on the right: append newInterval and all remaining intervals
    otherwise, merge into newInterval
3. append newInterval if not inserted yet
4. return result
T: O(n) | S: O(n)
'''

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            interval = intervals[i]
            if interval[1] < newInterval[0]:
                res.append(interval)
            elif interval[0] > newInterval[1]:
                res.append(newInterval)
                return res + intervals[i:]
            else:
                newInterval = [
                    min(interval[0], newInterval[0]),
                    max(interval[1], newInterval[1])
                ]
        res.append(newInterval)
        return res
        