class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        result = 0

        left = 0 

        for right in range(len(s)): 
            while s[right] in char_set: # meaning its a duplicate 
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])

            result = max(result, right - left + 1)

        return result
        
