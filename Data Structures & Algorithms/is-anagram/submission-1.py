class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        count_t = {}

        for char in s: 
            count_s[char] = 1 + count_s.get(char, 0)
            
        for char in t: 
            count_t[char] = 1 + count_t.get(char, 0)

        return count_s == count_t