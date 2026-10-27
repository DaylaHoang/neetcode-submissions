# Plan
# 1. Return 0 if the string starts with '0'
# 2. Intialize two_back = 1 and one_back = 1
# 3. Iterate from index 1 to the end, using DP formula: dp[i] = dp[i-1]+ dp[i-2]
# 4. If the current digit is != 0 -> add one_back
# 5. If the last 2 digits from 10-26 -> add two_back
# 6. Shift the 2 DP values forward
# 7. Return one_back
# T O(n) | S O(1)

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        # Ways to decode the empty prefix and the first digit
        two_back = 1
        one_back = 1
        for i in range(1, len(s)):
            current = 0
            # Option 1: Decode the current digit alone (1-9)
            if s[i] != '0':
                current += one_back
            # Option 2: Decode the last 2 digits together (10-26)
            if 10 <= int(s[i - 1: i + 1]) <= 26:
                current += two_back
            # Move forward to the next position
            two_back, one_back = one_back, current
        return one_back