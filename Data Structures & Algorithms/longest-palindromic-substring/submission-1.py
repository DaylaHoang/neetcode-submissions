# Plan
# 1. Track start and max_length of the longest palindrome
# 2. For eery index i, consider 2 centers
# 3. Odd center: left, right = i, i | Even center left, right = i, i+ 1
# 4. While pointers are in bounds and characters match, update the longest palindrome and move outward
# 5. Return s[start:start + max_length]

class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        max_length = 0
        
        for i in range(len(s)):
            for left, right in ((i, i), (i, i + 1)):
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    current_length = right - left + 1
                    # Save the longest palindrome found so far
                    if current_length > max_length:
                        start = left
                        max_length = current_length
                    # Expand outward from the center
                    left -= 1
                    right += 1
        return s[start:start + max_length]