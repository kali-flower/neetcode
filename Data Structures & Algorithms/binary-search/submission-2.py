class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        find mid 
        if target -> return 
        if target < mid -> search left (left to mid - 1)
        if target > mid -> search right (mid + 1 to right)
        if not found: return - 1
        '''

        left, right = 0, len(nums) - 1

        while left <= right: 
            mid = (left + right) // 2
            if nums[mid] == target: 
                return mid 
            elif nums[mid] > target: 
                right = mid - 1
            elif nums[mid] < target: 
                left = mid + 1 

        return -1
