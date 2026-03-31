class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        go through every row and every column ROWS = len(grid), COLS = len(grid[0])
        need a deque for exploration 
        if we see a 1 --> change to 0
        check its neighbors (up down right left)
        bounds check on neighbors (out of bounds), if out of bounds move on
        if 0, no need to add 
        otherwise, its a 1 --> add to queue to be explored and change to 0 
        '''

        islands = 0 
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(r, c): 
            q = deque() 
            grid[r][c] = "0"
            q.append((r, c))

            while q: 
                row, col = q.popleft()
                for dr, dc in directions: 
                    nr, nc = dr + row, dc + col

                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == "0"): 
                        continue 
                    else: # case where it's a 1 
                        q.append((nr, nc))
                        grid[nr][nc] = "0"

        for r in range(ROWS): 
            for c in range(COLS): 
                if grid[r][c] == "1": 
                    bfs(r, c)
                    islands += 1

        return islands     
    