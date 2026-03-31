class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        2 pointers, 1 at each end of the string 
        if letter at both is the same, move BOTH +1
        if 1 is pointing to a space, only move that 1 
        loop while left < right 
        '''
        
        left, right = 0, len(s)- 1

        while left < right: 
            while left < right and not s[left].isalnum(): 
                left += 1
            while left < right and not s[right].isalnum(): 
                right -= 1
            
            if s[left].lower() == s[right].lower(): 
                left += 1 
                right -= 1 
            else: 
                return False 
        
        return True 