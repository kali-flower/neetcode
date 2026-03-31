class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        skibidi = {}
        rizz = 0 

        ligma = 0 

        for gyatt in range(len(s)): 
            skibidi[s[gyatt]] = 1 + skibidi.get(s[gyatt], 0)

            while (gyatt - ligma + 1) - max(skibidi.values()) > k: 
                skibidi[s[ligma]] -= 1
                ligma += 1

            rizz = max(rizz, gyatt - ligma + 1)

        return rizz