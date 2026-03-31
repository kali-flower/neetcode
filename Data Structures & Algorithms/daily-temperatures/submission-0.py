class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # pair with [temp, index] at 0 and 1 

        for i, t in enumerate(temperatures): # get idx AND temp 
            while stack and t > stack[-1][0]: # is stack empty, and is our value greater than top of stack?
                temp, idx = stack.pop()
                result[idx] = (i - idx) # add the index to corresponding position 
            stack.append([t, i]) # append current t and i AFTER
            
        return result 
