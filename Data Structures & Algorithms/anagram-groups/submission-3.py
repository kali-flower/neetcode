class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strings = defaultdict(list)

        # for s in strs: 
            # sorted_s = ''.join(sorted(s))
            # strings[sorted_s].append(s)

        # return list(strings.values())

        # woke solution: 

        for s in strs: 
            count = [0] * 26 
            for c in s: 
                count[(ord(c) - ord('a'))] += 1

            strings[tuple(count)].append(s)

        return list(strings.values())
        