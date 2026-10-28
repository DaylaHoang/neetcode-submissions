# Plan
# 1. Convert wordDict into a set to check whether a word exists efficiently
# 2. Create dp of length n + 1 to track whether each prefix can be segmented
# 3. Set dp[0] = True -> empty prefix is valid
# 4. For each ending position end, determine whether the prefix ending there is valid
# 5. Try every starting position start to find a valid last word
# 6. check dp[start] and dp[start:end]
# 7. Return dp[n]
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict) # Fast dictionary lookup
        n = len(s)
        # dp[i] = Can the  first i characters be segmented?
        dp = [False] * (n + 1)
        dp[0] = True # Empty string is valid
        # Try building prefixes of length 1, 2, 3,.., n
        for end in range(1, n + 1):
            # Try every possible starting position of the last word
            for start in range(end):
                # Previous part must be valid AND last word must exist
                if dp[start] and s[start:end] in words:
                    dp[end] = True
                    break # Fond a valid split; no need to try more
        return dp[n]
        