class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        each half of the array (rotated vs not rotated) is still sorted 
        if left < right --> array already sorted 
        5 6 7 1 2 3 4 
        '''

        left, right = 0, len(nums) - 1 
        result = nums[0]

        while left <= right: 
            if nums[left] < nums[right]: 
                result = min(result, nums[left])
                break 
            mid = (left + right) // 2 
            result = min(result, nums[mid])

            if nums[mid] > nums[right]: 
                left = mid + 1 
            else: 
                right = mid - 1

        return result 