class Solution:
    from collections import defaultdict
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        need, have = [0] * 26, [0] * 26
        for ch in s1:
            need[ord(ch) - 97] += 1
        for i, ch in enumerate(s2):
            have[ord(ch) - 97] += 1
            if i >= len(s1):
                left_char = s2[i - len(s1)]
                have[ord(left_char) - 97] -= 1
            if need == have: return True
        return False
