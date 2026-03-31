class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False 

        count_s = {}
        count_t = {}

        for char in s: 
            if char not in count_s: 
                count_s[char] = 0 
            count_s[char] += 1 

        for char in t: 
            if char not in count_t: 
                count_t[char] = 0 
            count_t[char] += 1

        return count_s == count_t