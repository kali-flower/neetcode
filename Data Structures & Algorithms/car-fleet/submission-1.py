class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # create array of pairs and then sort it (by position, smallest first)
        pairs = [[pos, spd] for pos, spd in zip(position, speed)] 
        pairs.sort() 

        stack = [] # result will be len(stack)

        for pos, spd in pairs[::-1]: 
            stack.append((target - pos) / spd)

            if len(stack) >= 2 and stack[-2] >= stack[-1]: 
                stack.pop() 

        return len(stack)
