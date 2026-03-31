class Solution:
    def isValid(self, s: str) -> bool:
        '''
        if opening parentheses: push onto stack 
        if closing, and the top of the stack is a 
        matching parens and stack not empty: pop
        if stack empty at the end: return true 
        else: return false 
        ({()})
        '''   

        open = {"(", "[", "{"} # dict for opening parens 
        stack = []

        for item in s: 
            if item in open: 
                stack.append(item)
            elif item == ")" and stack and stack[-1] == "(": 
                stack.pop() 
            elif item == "]" and stack and stack[-1] == "[": 
                stack.pop() 
            elif item == "}" and stack and stack[-1] == "{": 
                stack.pop() 
            else: 
                return False 
        
        return not stack

            
