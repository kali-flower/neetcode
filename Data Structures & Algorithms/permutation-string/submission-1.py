class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # permutation = same letters, different order 
        # window = length of s1 

        count1 = {}
        for s in s1: 
            count1[s] = 1 + count1.get(s, 0)

        needed = len(count1)

        for i in range(len(s2)): 
            count2 = {}
            curr = 0 

            for j in range(i, len(s2)): 
                count2[s2[j]] = 1 + count2.get(s2[j], 0)
                if count1.get(s2[j], 0) < count2.get(s2[j]): 
                    break
                if count1.get(s2[j], 0) == count2[s2[j]]: 
                    curr += 1
                if curr == needed: 
                    return True
        
        return False