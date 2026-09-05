# Approach: 1. merge both arrays into a single list
# 2. Sort the merged list
# 3. Compute:
#   if odd, return the middle element
#   if even, return the average of the 2 middle median

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        merged.sort()
        total_number = len(merged)

        if total_number % 2 == 0:
            # 1, 2, 3 ,4
            # 0, 1, 2, 3
            return (merged[total_number // 2 - 1] + merged[total_number // 2]) / 2.0
        else: 
            return (merged[total_number // 2])




