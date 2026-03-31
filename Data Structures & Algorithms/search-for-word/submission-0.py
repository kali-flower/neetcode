class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set() 

        def dfs(r, c, i): # pass in row, col, and letter we are CURRENTLY looking for    
            if i == len(word): 
                return True 
            # bad case(s): out of bounds, letter we're looking at is wrong, or visiting same position twice
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or (r, c) in path): 
                return False 

            # if above conditions aren't met, we found a character we need
            path.add((r, c)) # add it to path set 
            # run dfs on ALL adjacent positions 
            result = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1))
            path.remove((r, c))

            return result 

        for r in range(ROWS): 
            for c in range(COLS): 
                if dfs(r, c, 0): 
                    return True 

        return False 