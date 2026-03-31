class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = [] # result array 

        def dfs(i, curr, total): # i = pointer, curr = current list, total = total running sum
            if total == target: 
                result.append(curr.copy()) # store a copy because if we modify curr, the result will be modified too 
                return 
            if i >= len(nums) or total > target: 
                return  

            # we include the current candidate (nums[i])
            curr.append(nums[i])
            dfs(i, curr, total + nums[i])

            curr.pop() 
            dfs(i + 1, curr, total)

        dfs(0, [], 0)
        return result 