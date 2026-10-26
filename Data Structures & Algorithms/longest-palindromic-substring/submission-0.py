# Plan
# 1. Track start and max_length of the longest palindrome
# 2. For eery index i, consider 2 centers
# 3. Odd center: left, right = i, i | Even center left, right = i, i+ 1
# 4. While pointers are in bounds and characters match, update the longest palindrome and move outward
# 5. Return s[start:start + max_length]

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start = 0
        max_length = 0
        
        def expand(left, right):
            nonlocal start, max_length
            while left >= 0 and right < n and s[left] == s[right]:
                length = right - left + 1
                if length > max_length:
                    start = left
                    max_length = length
                left -= 1
                right += 1
        for i in range(n):
            expand(i, i) # Odd-length
            expand(i, i + 1) # Even-length
        return s[start:start + max_length]