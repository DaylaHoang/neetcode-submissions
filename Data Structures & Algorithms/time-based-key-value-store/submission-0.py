# Maintain a map: key -> sorted list of (timestamp, value)
# set(key, value, timestamp): insert (timestamp, value) into the list for that key
# get(key, timestamp):
#   key doesn't exist -> ""
#   let times be sorted list, use binary search on times to find the rightmost index i such that time[i] <= timestamp
#       if exists -> return times[i]
#       if not, return ""


from sortedcontainers import SortedDict
class TimeMap:

    def __init__(self):
        self.m = defaultdict(SortedDict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.m:
            return ""
        
        timestamps = self.m[key]
        idx = timestamps.bisect_right(timestamp) - 1

        if idx >=0:
            clostest_time = timestamps.iloc[idx]
            return timestamps[clostest_time]
        else: return ""

        
