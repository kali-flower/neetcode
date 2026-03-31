class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = {}

        for num in nums: 
            if num not in counts: 
                counts[num] = 0 
            counts[num] += 1 

        for val in counts.values(): 
            if val > 1: 
                return True 

        return False