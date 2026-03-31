class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0 # if we get empty subarray, return 0 

        # [rob1, rob2, n, n + 1, ...]
        for n in nums: 
            temp = max(n + rob1, rob2)
            rob1 = rob2 
            rob2 = temp 
        return rob2 # rob2 will be equal to the last value 