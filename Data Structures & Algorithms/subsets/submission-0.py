class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [] 

        curr = []
        
        def dfs(i): 
            if i >= len(nums):
                result.append(curr.copy()) # if i ever goes out of bounds, we found a subset
                return 

            # include nums[i]
            curr.append(nums[i])
            dfs(i + 1)

            # don't include 
            curr.pop()
            dfs(i + 1)

        dfs(0)
        return result 