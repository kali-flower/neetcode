class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        goal = []
        n = len(nums)

        def backtrack(i, curr_sum): # i = number we are considering using 
        # curr_sum = partial solution from branch of tree 
            if curr_sum == target: 
                result.append(goal[:]) # appends a shallow copy 
                return 
            if curr_sum >= target or i == n: 
                return 

            backtrack(i + 1, curr_sum)

            goal.append(nums[i])
            backtrack(i, curr_sum + nums[i])
            goal.pop()

        backtrack(0, 0)
        return result
