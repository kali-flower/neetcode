class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1 # goal initially at the end 
        
        for i in range(len(nums) - 1, -1, -1): # start from end, go to the beginning 
            if i + nums[i] >= goal: 
                goal = i 

        if goal == 0: 
            return True 
        else: 
            return False 