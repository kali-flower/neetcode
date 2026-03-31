class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        sort input array 
        if left + 1 already in input array -> skip over it 
        2 pointers --> if perfect sum, add to result 
        if too big: shift right 
        if too small: shift left 
        while left < right 
        '''
        result = []
        nums.sort()

        for i, num in enumerate(nums): 
            if i > 0 and num == nums[i - 1]: # not the 1st value AND equal to its neighbor
                continue 

            left, right = i + 1, len(nums) - 1 # number after i 
            while left < right: 
                threeSum = num + nums[left] + nums[right]
                
                if threeSum > 0: 
                    right -= 1
                elif threeSum < 0: 
                    left += 1 
                else: 
                    result.append([num, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]: 
                        left += 1

        return result 