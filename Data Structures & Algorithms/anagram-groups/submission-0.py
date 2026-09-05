class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) # Creates a dictionary where every key starts with an empty listm, looks like {}
        for s in strs:
            sortedstring = ''.join(sorted(s))
            result[sortedstring].append(s)
        return list(result.values())


        