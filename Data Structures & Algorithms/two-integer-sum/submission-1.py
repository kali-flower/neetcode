class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        if we've already seen the number before, we want to look for it 
        1 2 3 7 4, t = 9 --> target - 2 = 7, not in dict so add 2 
        9 - 7 = 2, found in dict so return it :D
        '''

        seen = {}

        for i, num in enumerate(nums): 
            diff = target - num 
            if diff in seen: 
                return [seen[diff], i]
            else: 
                seen[num] = i 
