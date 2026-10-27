# Plan
# 1. Initialize count = 0 to track the number of palindromic substrings
# 2. Iterate through each index as a possible center
# 3. Check odd center (i, i) and even center (i, i + 1)
# 4. While the characters match, increment count and expand outward
# 5. Return count
# T: O(n^2) | S: O(1)
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            for left, right in ((i, i), (i, i + 1)):
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    count += 1
                    left -= 1
                    right += 1
        return count