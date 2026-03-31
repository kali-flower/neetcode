class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        longest substring that has at most k different characters 
        need to track characters we've already seen 
        ABAACA k = 1 --> include B, then when we get to c shrink window 
        replace character occuring less frequently   
        window size - MOST frequent character <= k 
        if greater, we need to do more replacements 
        for right in range(s): 
            add s[right] to map 

        '''

        result = 0 
        chars = set(s)

        for char in chars: # char = "dominant" character that wont be replaced
            count, left = 0, 0 

            for right in range(len(s)): 
                if s[right] == char: 
                    count += 1 
                
                while (right - left + 1) - count > k: 
                    if s[left] == char: 
                        count -= 1
                    left += 1 

                result = max(result, right - left + 1)

        return result