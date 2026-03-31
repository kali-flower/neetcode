class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        1 indexed (remember to add 1)
        sorted -> if left + right < target, left ++ 
        elif > target right -- 
        else return left + 1, right + 1
        '''

        left, right = 0, len(nums) - 1

        while left < right: 
            val = nums[left] + nums[right]
            if val < target:
                left += 1
            elif val > target: 
                right -= 1 
            else: 
                return [left + 1, right + 1]