class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []

        def backtrack(o, c): 
        # base case = proper parentheses 
            if o == c == n: 
                result.append("".join(stack)) # join every char in stack into string
                return 

            if o < n: 
                stack.append("(")
                backtrack(o + 1, c)
                stack.pop() # if return from backtracking, make sure we pop from stack 
            
            if c < o: 
                stack.append(")")
                backtrack(o, c + 1)
                stack.pop() 

        backtrack(0, 0)
        return result