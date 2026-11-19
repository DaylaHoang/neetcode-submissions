"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start) # sort asc
        heap = [] # store end time each room, only end time
        for interval in intervals:
            start = interval.start
            end = interval.end
            # heap[0] = time of the earliest available room
            if heap and start >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, end)
        return len(heap)
