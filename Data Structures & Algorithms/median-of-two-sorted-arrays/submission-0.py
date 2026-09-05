# Approach: 1. merge both arrays into a single list
# 2. Sort the merged list
# 3. Compute:
#   if odd, return the middle element
#   if even, return the average of the 2 middle median

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        merged.sort()

        totalLen = len(merged)
        if totalLen % 2 == 0:
            return (merged[totalLen // 2 - 1] + merged[totalLen // 2]) / 2.0
        else: return merged[totalLen // 2]