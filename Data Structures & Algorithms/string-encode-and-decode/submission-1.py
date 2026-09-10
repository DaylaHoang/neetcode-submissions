# Plan
# 1. Encode the string as length#string
# 2. Concatenate all encoded pieces
# 3. Decode by reading the length before each string
# 4. Move the pointer to next encoded string

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_parts = []

        for string in strs:
            encoded_parts.append(str(len(string)) + "#" + string)
        
        return "".join(encoded_parts)


    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            delimiter_index = s.find("#", i)
            length = int(s[i:delimiter_index])
            string_start = delimiter_index + 1
            string = s[string_start:string_start + length]

            result.append(string)
            i = string_start + length
        return result



