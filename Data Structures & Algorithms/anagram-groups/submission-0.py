class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strings = defaultdict(list)

        for s in strs: 
            sorted_s = ''.join(sorted(s))
            strings[sorted_s].append(s)

        return list(strings.values())
        