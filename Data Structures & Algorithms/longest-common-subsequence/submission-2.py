'''
Plan
1. Define a 2D DP table (prefix lengths as my DP state)
dp[i][j] = LCS length of text1[:i] and text2[:j]
2. Initialize the base cases
dp = (m+1) * (n+1), filled with 0
3. If characters match, I'll extend the diagonal result because both characters can be included. Otherwise I'll skip one character and keep whichever previous result is longer
4. Return dp[m][n]
'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for i in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]