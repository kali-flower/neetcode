class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        if the curr num - 1 is in the array -> its not the start of a seq
        if it has no left neighbor -> start of a sequence, and look for the consecutive numbers 
        add everything to set 
        if start of sequence, check for the +1s in the set 
        0 1 2 3 4 
        '''

        seen = set(nums)
        longest =  0

        for num in nums: 
            if num - 1 not in seen: # start of sequence 
                length = 1 
                while num + length in seen: 
                    length += 1 
                
                longest = max(longest, length)

        return longest 