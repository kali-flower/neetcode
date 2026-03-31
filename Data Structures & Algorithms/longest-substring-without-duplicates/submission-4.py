class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        start both pointers at the same place 
        loop through entire string
        track characters that we've seen
        if there's a non dupe, we're good 
        while there are duplicates, shrink the window
        calc window size for each iteration and update the max 
        '''

        seen = set() 
        result = 0 
        left = 0 

        for right in range(len(s)): 
            while s[right] in seen: 
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            result = max(result, right - left + 1)
        return result 