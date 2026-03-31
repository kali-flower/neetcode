class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] 
        # could be 1 of the 4 operators, or it could be an int 
        # for - and / the order we are popping in is not the order we want to apply the operation 
        for item in tokens: 
            if item == "+": 
                stack.append(stack.pop() + stack.pop())
            elif item == "-":
                stack.append(-(stack.pop() - stack.pop()))
            elif item == "*": 
                stack.append(stack.pop() * stack.pop())
            elif item == "/": 
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else: # case where it is an int 
                stack.append(int(item))

        return stack[0]