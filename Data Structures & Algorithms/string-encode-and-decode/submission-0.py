class Solution:
# count the length of each value in the list, remember that to decode later
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
            # length#word
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while len(s) > i:
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res
        
