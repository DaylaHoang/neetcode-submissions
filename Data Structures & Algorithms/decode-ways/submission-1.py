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
        prev2 = 1 # dp[0]=1 -> empty string has 1 way to decode
        prev1 = 0 if s[0] == "0" else 1 #dp[1]:0 ways if first digit is "0", otherwise 1
        for i in range(2, len(s)+1):
            current = 0 #dp[i]: number of ways to decode the first i characters
            #Case 1: decode 1 digit (1-9)
            if s[i-1] != "0":
                current += prev1
            if 10 <= int(s[i-2: i]) <=26:
                current += prev2
            # Shift DP states forward for the next iteration
            prev2 = prev1
            prev1 = current
        return prev1
