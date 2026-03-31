class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        sliding window 
        start at 1st element 
        if next char is different --> expand window 
        need to know when we find duplicate --> keep a set 
        if dupe found, shrink window until no more dupes, then continue  
        '''
        left = 0
        max_len = 0 
        seen = set()

        for right in range(len(s)): 
            while s[right] in seen: 
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len 
