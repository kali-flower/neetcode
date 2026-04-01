class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # target - nums[i] has to be nums[j]
        # for each element -> if target - that element exists in hashmap, then return the idx where the diff is 
        # so map should store idx: value, and check if target - num in map.values()
        
        diffs = {}
        for i in range(len(nums)): 
            result = target - nums[i]
            if result in diffs: 
                return [diffs[result], i]
            diffs[nums[i]] = i 

        return []