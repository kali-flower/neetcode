class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right: 
            mid = (left + right) // 2
            if target == nums[mid]: 
                return mid 

            if nums[mid] >= nums[left]: # left sorted portion 
                if target > nums[mid] or target < nums[left]: # need to search to the RIGHT
                    left = mid + 1
                else: # less than mid, greater than left 
                    right = mid - 1
            else: # right sorted portion 
                if target < nums[mid] or target > nums[right]: #search to the left
                    right = mid - 1 
                elif target > nums[mid]: # search left 
                    left = mid + 1 

        return -1