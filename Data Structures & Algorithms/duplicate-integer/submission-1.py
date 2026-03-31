class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # make counts hashmap, add everything 
        # if any count greater than 1, return true 

        counts = {}

        for num in nums: 
            counts[num] = 1 + counts.get(num, 0)

        for val in counts.values(): 
            if val > 1: 
                return True

        return False 